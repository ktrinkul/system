from fastapi import APIRouter, HTTPException
from typing import List
from .models import Scenario, ScenarioIn

router = APIRouter()

@router.post('/', response_model=Scenario)
async def create_scenario(scenario: ScenarioIn) -> Scenario:
    """Creates a new scenario."""
    try:
        new_scenario = Scenario.create(scenario)
        return new_scenario
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle value error gracefully

@router.get('/{scenario_id}', response_model=Scenario)
async def get_scenario(scenario_id: str) -> Scenario:
    """Retrieves a scenario by ID."""
    try:
        scenario = Scenario.get(scenario_id)
        return scenario
    except ScenarioNotFound:
        raise HTTPException(status_code=404, detail='Scenario not found')