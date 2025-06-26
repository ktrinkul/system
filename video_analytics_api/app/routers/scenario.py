from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app import models, schemas
from typing import List

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/scenario/", response_model=schemas.ScenarioOut)
async def create_scenario(scenario: schemas.ScenarioCreate, db: AsyncSession = Depends(get_db)):
    new_scenario = models.Scenario(video_path=scenario.video_path)
    db.add(new_scenario)
    await db.flush()  # Чтобы получить ID нового сценария до коммита

    # 📤 Добавляем событие в Outbox
    outbox_event = models.OutboxEvent(
        event_type="Scenario_ScenarioStatus.in_startup_processing",
        payload={"scenario_id": new_scenario.id, "status": "in_startup_processing"},
    )
    db.add(outbox_event)

    await db.commit()
    await db.refresh(new_scenario)
    return new_scenario


@router.post("/scenario/{scenario_id}/", response_model=schemas.ScenarioOut)
async def update_scenario(scenario_id: int, update: schemas.ScenarioUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Scenario).where(models.Scenario.id == scenario_id))
    scenario = result.scalar_one_or_none()
    if scenario is None:
        raise HTTPException(status_code=404, detail="Scenario not found")
    scenario.status = update.status
    await db.commit()
    await db.refresh(scenario)
    return scenario

@router.get("/scenario/{scenario_id}/", response_model=schemas.ScenarioOut)
async def get_scenario(scenario_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Scenario).where(models.Scenario.id == scenario_id))
    scenario = result.scalar_one_or_none()
    if scenario is None:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scenario

@router.get("/prediction/{scenario_id}/", response_model=List[schemas.PredictionOut])
async def get_predictions(scenario_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Prediction).where(models.Prediction.scenario_id == scenario_id))
    return result.scalars().all()
