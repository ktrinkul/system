from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FrameDetection(Base):
    __tablename__ = "frame_detections"

    id = Column(Integer, primary_key=True, index=True)
    video_path = Column(String, index=True)  # путь к видео или id видео
    frame_number = Column(Integer, index=True)
    detections = Column(JSON)  # JSON с результатами детекции

class VideoProgress(Base):
    __tablename__ = "video_progress"

    id = Column(Integer, primary_key=True, index=True)
    video_path = Column(String, unique=True, index=True)
    last_processed_frame = Column(Integer, default=0)
