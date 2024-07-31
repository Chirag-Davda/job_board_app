from sqlalchemy import Column,Integer,String,Boolean,DateTime
from database.database import Base
from datetime import datetime
import uuid
class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    user_name = Column(String(20),nullable=False)
    Mobile_No = Column(String(10),nullable=False)
    email = Column(String(30),nullable=False)
    password = Column(String(200), nullable = False)
    Date_of_Birth = Column(String(20),nullable=False)
    Gender = Column(String(20),nullable=False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    is_verified = Column(Boolean , default= False)