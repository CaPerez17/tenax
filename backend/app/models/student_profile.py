from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, Enum
from sqlalchemy.sql import func
from app.database.database import Base
import enum

class StudyStyle(enum.Enum):
    VISUAL = "visual"
    AUDITORY = "auditory"
    KINESTHETIC = "kinesthetic"
    MIXED = "mixed"

class StudentSystemProfile(Base):
    __tablename__ = "student_system_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False, index=True)
    study_style = Column(Enum(StudyStyle), nullable=False)
    preferred_times = Column(JSON, nullable=True)
    tools_connected = Column(JSON, nullable=True)
    goals = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
