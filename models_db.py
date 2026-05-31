from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    email=Column(String,unique=True)
    password=Column(String)

class UsersData(Base):
    __tablename__='usersdata'
    id=Column(Integer,primary_key=True,autoincrement=True)
    problem_name=Column(String)
    topic=Column(String)
    difficulty=Column(String)
    entry_date=Column(Date)
    user_id = Column(Integer, ForeignKey('user.id'))
    def to_dict(self):
        return {
            'problem_name': self.problem_name,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'entry_date': str(self.entry_date),
            'user_id': self.user_id
        }