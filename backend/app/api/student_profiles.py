from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import SessionLocal
from app.models.student_profile import StudentSystemProfile
from app.schemas.student_profile import (
    StudentSystemProfileCreate,
    StudentSystemProfileResponse,
    StudentSystemProfileUpdate
)

router = APIRouter(prefix="/student-profiles", tags=["student-profiles"])

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=StudentSystemProfileResponse)
def create_student_profile(
    profile: StudentSystemProfileCreate,
    db: Session = Depends(get_db)
):
    """Create a new student profile"""
    db_profile = StudentSystemProfile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@router.get("/{profile_id}", response_model=StudentSystemProfileResponse)
def get_student_profile(
    profile_id: int,
    db: Session = Depends(get_db)
):
    """Get a student profile by ID"""
    profile = db.query(StudentSystemProfile).filter(
        StudentSystemProfile.id == profile_id
    ).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return profile

@router.get("/", response_model=List[StudentSystemProfileResponse])
def list_student_profiles(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List student profiles"""
    profiles = db.query(StudentSystemProfile).offset(skip).limit(limit).all()
    return profiles 