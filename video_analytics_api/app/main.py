from fastapi import FastAPI
from app.routers import scenario
from app.routers import outbox
from app.database import Base, engine

app = FastAPI()

app.include_router(scenario.router)
app.include_router(outbox.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
