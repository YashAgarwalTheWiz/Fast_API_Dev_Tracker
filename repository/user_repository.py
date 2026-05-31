from models import user,login_user
from passlib.hash import bcrypt
from database import SessionLocal
from models_db import User

def insert_user(user:user):
    try:
        db=SessionLocal()
        hashed_pass = bcrypt.hash(user.password)
        new_user=User(name=user.name,email=user.email,password=hashed_pass)
        db.add(new_user)
        db.commit()
        return "success"
    except Exception as e:
        return str(e)
    finally:
        db.close()


def get_user_id(email:str):
    db=SessionLocal()
    user_row=db.query(User).filter(User.email==email).first()
    db.close()
    return user_row.id


def login_user_dao(user:login_user):
    db=SessionLocal()
    data=db.query(User).filter(User.email==user.email).first()
    if not data:
        return None
    is_valid = bcrypt.verify(user.password, data.password)
    db.close()
    if is_valid:
        return data
    return None
