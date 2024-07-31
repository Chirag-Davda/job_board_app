from datetime import datetime, timedelta
from fastapi import HTTPException, status, Security
from dotenv import load_dotenv
import os
from jose import JWTError, jwt

load_dotenv()

SECRET_KEY = str(os.environ.get("SECRET_KEY"))
ALGORITHM = str(os.environ.get("ALGORITHM"))

def get_token(id, user_name,email):
    payload = {
        "user_id": id,
        "user_name" : user_name,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=5),
    }
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(type(access_token))
    return access_token



def decode_token_user_id(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
def decode_token_user_email(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("user_email")
        if not user_email:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return user_email
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
def decode_token_user_name(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name = payload.get("user_name")
        if not user_name:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return user_name
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
    
def logging_token(id:str, user_name:str,email:str):
    payload = {
        "user_id": id,
        "user_name" : user_name,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=50),
    }
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    # print(type(access_token))
    return access_token









