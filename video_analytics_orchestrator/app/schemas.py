from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from typing import Any, Dict

class ScenarioStatus(str, Enum):
    init_startup = "init_startup"
    in_startup_processing = "in_startup_processing"
    active = "active"
    init_shutdown = "init_shutdown"
    in_shutdown_processing = "in_shutdown_processing"
    inactive = "inactive"

class ScenarioEvent(BaseModel):
    scenario_id: int
    target_status: ScenarioStatus

class OutboxEventSchema(BaseModel):
    id: int
    aggregate_id: int
    event_type: str
    payload: Dict[str, Any]
    processed: bool
    created_at: datetime

    class Config:
        orm_mode = True
