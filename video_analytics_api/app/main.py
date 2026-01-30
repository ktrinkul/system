from fastapi import FastAPI
from .services import create_scenario, get_scenario_status

app = FastAPI()

@app.post('/scenario/')
async def create_new_scenario(data: dict):
    return create_scenario(data)

@app.get('/scenario/{scenario_id}/status')
async def status(scenario_id: int):
    return get_scenario_status(scenario_id)