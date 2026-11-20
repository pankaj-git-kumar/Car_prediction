from sqlalchemy.orm import Session
from . import models
from app.db.schemas import UserCreate
def get_all_users(db: Session):
    return db.query(models.User).all()

def get_employee_id(db: Session, emp_id: int):
    return (
        db
        .query(models.User)
        .filter(models.User.id == emp_id)
        .first()
    )

def get_employee_email(db: Session, email: str):
    return (
        db
        .query(models.User)
        .filter(models.User.email == email)
        .first()
    )


def authenticate_user(db: Session, email: str, password: str):
    user = get_employee_email(db, email)
    if not user:
        return False
    if not user.password == password:
        return False
    return user


def create_user(db: Session, user: UserCreate):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



