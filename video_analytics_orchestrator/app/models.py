from sqlalchemy import (
    Column, Integer, String, Enum, JSON, Boolean, DateTime, func
)
from app.database import Base
import enum

class ScenarioStatus(str, enum.Enum):
    init_startup = "init_startup"
    in_startup_processing = "in_startup_processing"
    active = "active"
    init_shutdown = "init_shutdown"
    in_shutdown_processing = "in_shutdown_processing"
    inactive = "inactive"

class ScenarioState(Base):
    __tablename__ = "scenario_state"
    id = Column(Integer, primary_key=True)  # совпадает с API-scenario.id
    status = Column(Enum(ScenarioStatus), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
