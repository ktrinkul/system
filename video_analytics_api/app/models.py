from sqlalchemy import Column, Integer, String, Enum, JSON
from sqlalchemy import Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base
import enum

class ScenarioStatus(str, enum.Enum):
    init_startup = "init_startup"
    in_startup_processing = "in_startup_processing"
    active = "active"
    init_shutdown = "init_shutdown"
    in_shutdown_processing = "in_shutdown_processing"
    inactive = "inactive"

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True, index=True)
    video_path = Column(String, nullable=False)
    status = Column(Enum(ScenarioStatus), default=ScenarioStatus.init_startup)

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    scenario_id = Column(Integer)
    data = Column(JSON)

class OutboxEvent(Base):
    __tablename__ = "outbox_events"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    processed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())