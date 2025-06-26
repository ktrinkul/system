from pydantic import BaseModel
from enum import Enum
from typing import Optional, List, Dict

class ScenarioStatus(str, Enum):
    init_startup = "init_startup"
    in_startup_processing = "in_startup_processing"
    active = "active"
    init_shutdown = "init_shutdown"
    in_shutdown_processing = "in_shutdown_processing"
    inactive = "inactive"

class ScenarioCreate(BaseModel):
    video_path: str

class ScenarioUpdate(BaseModel):
    status: ScenarioStatus

class ScenarioOut(BaseModel):
    id: int
    video_path: str
    status: ScenarioStatus

    class Config:
        orm_mode = True

class PredictionOut(BaseModel):
    id: int
    scenario_id: int
    data: Dict
