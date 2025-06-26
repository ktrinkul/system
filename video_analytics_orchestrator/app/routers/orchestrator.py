from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app import models, schemas, state_machine

router = APIRouter(prefix="/orchestrator")

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/scenario/", response_model=schemas.OutboxEventSchema)
async def init_scenario(event: schemas.ScenarioEvent, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    # 1) создаём/обновляем ScenarioState
    result = await db.execute(select(models.ScenarioState).where(models.ScenarioState.id == event.scenario_id))
    state = result.scalar_one_or_none()
    if not state:
        state = models.ScenarioState(id=event.scenario_id, status=event.target_status)
        db.add(state)
    else:
        # FSM
        fsm = state_machine.ScenarioFSM(state.status)
        fsm.next(event.target_status)
        state.status = fsm.state
    # 2) записываем событие в Outbox
    out = models.OutboxEvent(
        aggregate_id=event.scenario_id,
        event_type=f"Scenario_{event.target_status}",
        payload={"status": event.target_status.value}
    )
    db.add(out)
    await db.commit()
    await db.refresh(out)
    # 3) фоновая задача запустит публикацию
    background_tasks.add_task(publish_outbox)
    return out

# stub публикации
async def publish_outbox():
    from app.database import SessionLocal
    from app.models import OutboxEvent
    from aiokafka import AIOKafkaProducer
    import asyncio

    # создаём producer
    producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")
    await producer.start()
    async with SessionLocal() as session:
        q = await session.execute(select(OutboxEvent).where(OutboxEvent.processed == False))
        events = q.scalars().all()
        for ev in events:
            # отправляем в Kafka
            await producer.send_and_wait("scenario_events", value=ev.payload)
            ev.processed = True
        await session.commit()
    await producer.stop()
