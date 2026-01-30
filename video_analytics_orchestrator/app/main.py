from fastapi import FastAPI
from app.database import engine, Base
from app.routers import orchestrator

app = FastAPI(title="Orchestrator")

@app.get("/health")
async def health_check():
    return {"status": "operational"}

app.include_router(orchestrator.router)

@app.on_event("startup")
async def on_start():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # Additional orchestration setup can be done here