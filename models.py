from pydantic import BaseModel
from datetime import date

class data(BaseModel):
    problem_name:str
    topic:str
    difficulty:str
    entry_date:date

class user(BaseModel):
    name:str
    email:str
    password:str

class login_user(BaseModel):
    email:str
    password:str