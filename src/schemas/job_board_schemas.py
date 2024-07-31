from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    title: str
    description: str
    company: str
    location: str

class JobCreate(JobBase):
    pass

class JobUpdate(JobBase):
    pass

