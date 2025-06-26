from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_async_session
from app.models import OutboxEvent

router = APIRouter(prefix="/outbox", tags=["Outbox"])

@router.get("/")
async def get_outbox_events(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(OutboxEvent).order_by(OutboxEvent.created_at.desc()).limit(10))
    events = result.scalars().all()
    return events
