from fastapi import FastAPI
from .services import initialize_scenario, update_scenario_status

app = FastAPI()

@app.post('/scenario/')
async def start_scenario():
    return initialize_scenario()

@app.post('/scenario/{scenario_id}/status')
async def change_status(scenario_id: int, status: str):
    return update_scenario_status(scenario_id, status)