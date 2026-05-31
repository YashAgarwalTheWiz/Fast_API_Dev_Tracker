from models import data
from models_db import User,UsersData
from database import SessionLocal
from sqlalchemy import func
from sqlalchemy import distinct

def insert_entries(data:data,user_id):
    db=SessionLocal()
    new_user=UsersData(problem_name=data.problem_name,topic=data.topic,difficulty=data.difficulty,entry_date=data.entry_date,user_id=user_id)
    db.add(new_user)
    db.commit()
    db.close()

def show_values():
    db=SessionLocal()
    data=db.query(User).all()
    db.close()
    return [row.to_dict() for row in data]

def filter_by_difficulty(difficulty:str,user_id):
    db=SessionLocal()
    data=db.query(UsersData.problem_name,UsersData.topic,UsersData.entry_date).filter(UsersData.difficulty==difficulty,UsersData.user_id==user_id).all()
    db.close()
    return [row._asdict() for row in data]
    
def get_difficulty_count(user_id):
    db=SessionLocal()
    data = db.query(func.count(UsersData.difficulty).label('count'),UsersData.difficulty).filter(UsersData.user_id == user_id).group_by(UsersData.difficulty).all()
    db.close()
    return [row._asdict() for row in data]


def show_single_user_value(user_id,page,limit):
    db=SessionLocal()
    data=db.query(UsersData).filter(UsersData.user_id==user_id).offset((page-1)*limit).limit(limit).all()
    db.close()
    return [row.to_dict() for row in data]

def piechartbytopic(user_id):
    db=SessionLocal()
    data = db.query(func.count(UsersData.topic).label('count'),UsersData.topic).filter(UsersData.user_id == user_id).group_by(UsersData.topic).all()
    db.close()
    return [row._asdict() for row in data]

def dates_user_active(user_id):
    db=SessionLocal()
    data=db.query(UsersData.entry_date).filter(UsersData.user_id==user_id).distinct().order_by(UsersData.entry_date).all()
    db.close()
    return [row._asdict() for row in data]


