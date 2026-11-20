from fastapi import FastAPI
# from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_login , routes_register
# from app.middleware.logging_middleware import LoggingMiddleware
# from app.core.exceptions import register_exception_handlers
from app.db import models
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)
import os
print("DB FILE:", os.path.abspath(engine.url.database))
print("TABLES:", list(Base.metadata.tables.keys()))

app = FastAPI(title='Car Price Prediction API')

# link middleware
# app.add_middleware(LoggingMiddleware)

# link endpoints
app.include_router(routes_login.router, tags=['Login'])
# app.include_router(routes_prediciton.router, tags=['Prediction'])
app.include_router(routes_register.router, tags=['Register'])
# monitoring using Prometheus
# Instrumentator().instrument(app).expose(app)

# add exception handler
# register_exception_handlers(app)