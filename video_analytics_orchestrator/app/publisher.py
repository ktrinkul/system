# video_analytics_orchestrator/app/publisher.py

import asyncio
import logging
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import OutboxEvent
from .database import get_async_session

logging.basicConfig(level=logging.INFO)

async def process_outbox():
    while True:
        async for session in get_async_session():
            await handle_unprocessed_events(session)
        await asyncio.sleep(3)

async def handle_unprocessed_events(session: AsyncSession):
    result = await session.execute(
        select(OutboxEvent).where(OutboxEvent.processed == False)
    )
    events = result.scalars().all()

    for event in events:
        logging.info(f"📤 Sending event: {event.event_type} for scenario {event.aggregate_id}")

        await session.execute(
            update(OutboxEvent)
            .where(OutboxEvent.id == event.id)
            .values(processed=True)
        )

    await session.commit()

if __name__ == "__main__":
    asyncio.run(process_outbox())
