
from fastapi import APIRouter, Depends, HTTPException, status
from app.db.schemas import UserLogin
from sqlalchemy.orm import Session
from app.db.curd_db import authenticate_user
from app.core.security import create_access_token
from app.db.database import get_db

router = APIRouter()
 
@router.post('/login')
def user_login(data:UserLogin, db:Session  = Depends(get_db)):
  user = authenticate_user(db , data.email ,  data.password)
  if user:
    token = create_access_token({
      'sub': str(user.id),
      'name': user.name })
    return token
  else:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",)

  