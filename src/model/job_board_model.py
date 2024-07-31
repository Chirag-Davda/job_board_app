from sqlalchemy import Column,Integer,String,Boolean,DateTime,Text,func
from database.database import Base
from datetime import datetime
import uuid

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(Text)
    company = Column(String(100))
    location = Column(String(100))
    posted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)