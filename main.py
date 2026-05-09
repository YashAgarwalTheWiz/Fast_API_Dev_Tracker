from fastapi import FastAPI,Depends
from models import data
from dao import insert_entries,show_values,filter_by_difficulty,get_difficulty_count,show_single_user_value,piechartbytopic,dates_user_active
from routers import auth
from auth_utils import get_current_user

app=FastAPI()

app.include_router(auth.router)

@app.get('/')
def hello():
    return {'message':'Hello world'}

@app.post('/insert_data')
def getdata(data:data,current_user: str = Depends(get_current_user)):
    insert_entries(data,current_user)
    return data

@app.get('/show_users')
def showuser(current_user:str=Depends(get_current_user)):
    return show_single_user_value(current_user)
    
@app.get('/filter_by_difficulty')
def filterby_difficulty(difficulty:str):
    data=filter_by_difficulty(difficulty)
    return data

@app.get('/count_by_difficulty')
def count_by_difficulty(currentuser:str=Depends(get_current_user)):
    res=get_difficulty_count(currentuser)
    return res

@app.get('/count_by_topic')
def count_by_topic(currentuser:str=Depends(get_current_user)):
    data=piechartbytopic(currentuser)
    return data

@app.get('/activedates')
def user_active(currentuser:str=Depends(get_current_user)):
    return dates_user_active(currentuser)
