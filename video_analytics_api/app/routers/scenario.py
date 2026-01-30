from fastapi import APIRouter, HTTPException
from .schemas import ScenarioInit, ScenarioUpdate
from .database import get_scenario_by_id, update_scenario_status

router = APIRouter()

@router.post('/scenario/', response_model=ScenarioInit)
async def initialize_scenario(scenario: ScenarioInit):
    try:
        # Implementation for initializing scenario
        pass  # Replace with actual implementation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/scenario/{scenario_id}/', response_model=ScenarioUpdate)
async def update_scenario(scenario_id: int, status: str):
    try:
        if not await get_scenario_by_id(scenario_id):
            raise HTTPException(status_code=404, detail='Scenario not found')
        # Implementation for updating scenario status
        update_status = await update_scenario_status(scenario_id, status)
        return update_status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))