from pydantic import BaseModel 

class StuBase(BaseModel):
    user_name : str
    Mobile_No : int
    email : str
    Date_of_Birth : str
    password : str
    Gender : str

class User_OTP(BaseModel):
    email : str
    
class OTP_Verify(BaseModel):
    email : str
    otp : str