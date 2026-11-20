from fastapi import APIRouter, Depends, HTTPException, status
# from Schemas.user_data import UserLogin
from sqlalchemy.orm import Session
from app.db.curd_db import  get_employee_email , create_user
from app.core.security import create_access_token
from app.db.database import get_db
from app.db.schemas import UserCreate
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post('/register')
def user_register(data:UserCreate , db:Session = Depends(get_db)):
  if get_employee_email(db, data.email):
    raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )
  else:
    try:
      create_user(db, data)
    except IntegrityError:
      db.rollback()
      raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )
    return {"message": "User successfully created"}

