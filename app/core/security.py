from app.core.config import setting
from datetime import datetime , timedelta, timezone
from authlib.jose import JoseError, jwt
from fastapi import HTTPException

def create_access_token(data: dict):
  user_data = data.copy()
  Header = {'alg': setting.JWT_ALGORITHM, 'typ': 'JWT'}
  Payload = user_data
  expire = datetime.now(timezone.utc) + timedelta(minutes=setting.EXPIRY_TIME)
  Payload["exp"] = int(expire.timestamp())
  return jwt.encode(Header, Payload, setting.JWT_SECRET_KEY)


def Verify_token(token:str):
  try:
     Payload = jwt.decode(token, setting.JWT_SECRET_KEY)
     if Payload:
       return Payload
     return HTTPException(status_code=401, detail='Invalid JWT Token')
  except JoseError:
    raise HTTPException(status_code=401,  detail="Couldn't Validate Credentials")