# app/apis/routes/users.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserOut
from app.models.user import User
from app.apis.deps import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserOut)
def read_users_me(
    current_user: User = Depends(get_current_user)
):
    return current_user
