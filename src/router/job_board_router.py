from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database.database import SessionLocal
from src.model.job_board_model import Job as JobModel
from database.database import SessionLocal
from passlib.context import CryptContext
from src.schemas.job_board_schemas import Job, JobCreate, JobUpdate

job_router = APIRouter()
Otp_router = APIRouter()
db = SessionLocal()

pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")


@job_router.post("/post_jobs/", response_model=JobCreate)
def create_job(job: JobCreate):
    db_job = JobModel(
        title = job.title,
        description = job.description,
        company = job.company,
        location = job.location
        
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@job_router.get("/get_jobs/", response_model=Job)
def read_job(job_id: int):
    db_job = db.query(JobModel).filter(JobModel.id == job_id, JobModel.is_active == True, JobModel.is_deleted == False).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@job_router.get("/all_jobs/", response_model=List[Job])
def read_jobs():
    db_jobs = db.query(JobModel).filter(JobModel.is_active == True, JobModel.is_deleted == False).all()
    if not db_jobs:
        raise HTTPException(status_code=404, detail="No jobs found")
    return db_jobs

@job_router.put("/update_jobs}", response_model=Job)
def update_job(job_id: int, job: JobUpdate):
    db_job = db.query(JobModel).filter(JobModel.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    for key, value in job.dict().items():
        setattr(db_job, key, value)
    
    db.commit()
    db.refresh(db_job)
    return db_job

@job_router.delete("/delet_jobs")
def delete_job(job_id: int,):
    db_job = db.query(JobModel).filter(JobModel.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    db_job.is_deleted = True
    db_job.is_active = False
    db.commit()
    return {"message": "Job deleted successfully"}
