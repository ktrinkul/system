import json
from fastapi import APIRouter, HTTPException
from ..models import Scenario, ScenarioCreate, ScenarioUpdate

router = APIRouter()

@router.post("/scenario/")
async def create_scenario(scenario: ScenarioCreate):
    """Create a new scenario."""
    new_scenario = Scenario(**scenario.dict())
    # Save scenario to database
    return new_scenario

@router.post("/scenario/{scenario_id}/status/")
async def update_scenario_status(scenario_id: int, status: str):
    """Update the status of a scenario."""
    existing_scenario = get_scenario_by_id(scenario_id)
    if existing_scenario is None:
        raise HTTPException(status_code=404, detail="Scenario not found")
    # Validate and update status
    if validate_status_transition(existing_scenario.status, status):
        existing_scenario.status = status
        # Update scenario in database
        return existing_scenario
    else:
        raise HTTPException(status_code=400, detail="Invalid status transition")

# Function to validate if the transition is allowed
def validate_status_transition(current_status: str, new_status: str) -> bool:
    """Check if the status transition is valid."""
    valid_transitions = {
        'init_startup': ['in_startup_processing', 'inactive'],
        'in_startup_processing': ['active', 'init_shutdown'],
        'active': ['init_shutdown'],
        'init_shutdown': ['inactive'],
    }
    return new_status in valid_transitions.get(current_status, [])
