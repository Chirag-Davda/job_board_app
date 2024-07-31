from sqlalchemy import Column,Integer,String,Boolean,DateTime
from database.database import Base
from datetime import datetime
import uuid

class Otp(Base):
    __tablename__ = "otp"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    email = Column(String(30),nullable=False)
    otp = Column(String(6),nullable = False)
    expires_at = Column(DateTime)
    created_at=Column(DateTime,default=datetime.now)