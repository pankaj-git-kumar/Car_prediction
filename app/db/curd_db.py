from sqlalchemy.orm import Session
import models, schemas

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

def create_employee(db: Session, user: schemas.EmployeeCreate):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



