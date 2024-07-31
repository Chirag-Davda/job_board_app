from fastapi import FastAPI,APIRouter
from src.router.user_router import User1
from src.router.user_router import Otp_router
from src.router.job_board_router import job_router

app = FastAPI()
app.include_router(User1)
app.include_router(Otp_router)
app.include_router(job_router)
