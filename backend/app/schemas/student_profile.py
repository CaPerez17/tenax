from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Dict, Any
from datetime import datetime
from app.models.student_profile import StudyStyle

class StudentSystemProfileBase(BaseModel):
    """Base schema for StudentSystemProfile"""
    user_id: str
    study_style: StudyStyle
    preferred_times: Optional[Dict[str, Any]] = None
    tools_connected: Optional[List[str]] = None
    goals: Optional[str] = None

class StudentSystemProfileCreate(StudentSystemProfileBase):
    """Schema for creating a new student profile"""
    pass

class StudentSystemProfileUpdate(BaseModel):
    """Schema for updating a student profile"""
    study_style: Optional[StudyStyle] = None
    preferred_times: Optional[Dict[str, Any]] = None
    tools_connected: Optional[List[str]] = None
    goals: Optional[str] = None

class StudentSystemProfileResponse(StudentSystemProfileBase):
    """Schema for API response"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True) 