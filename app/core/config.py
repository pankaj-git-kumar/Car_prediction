import os 
from dotenv import load_dotenv

load_dotenv()

class Settings():
  PROJECT_NAME = os.getenv('APP_NAME', 'Car Price API')
  API_KEY = os.getenv('API_KEY', 'demo-key')
  JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret')
  JWT_ALGORITHM = 'HS256'
  EXPIRY_TIME = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30)
  MODEL_PATH = 'app/models/model.joblib'
  REDIS_URL =  'redis://localhost:6379'
setting = Settings()
