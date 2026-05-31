from fastapi import FastAPI,Depends
from models import data
from services.problem_service import log_problem,get_filtered_by_difficulty,get_difficulty_stats,get_user_problems,get_topic_stats,get_active_dates
from routers import auth
from auth_utils import get_current_user
from contextlib import asynccontextmanager
from database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine) #creates all tables that are defined as classes inheriting from Base automatically
    yield

app=FastAPI(lifespan=lifespan)

app.include_router(auth.router)

@app.get('/')
def hello():
    return {'message':'Hello world'}

@app.post('/insert_data')
def getdata(data:data,current_user: str = Depends(get_current_user)):
    log_problem(data,current_user)
    return data

@app.get('/my_problems')
def showuser(page: int = 1, limit: int = 20, current_user: str = Depends(get_current_user)):
    return get_user_problems(current_user, page, limit)
    
@app.get('/filter_by_difficulty')
def filterby_difficulty(difficulty:str,current_user: str = Depends(get_current_user)):
    data=get_filtered_by_difficulty(difficulty,current_user)
    return data

@app.get('/count_by_difficulty')
def count_by_difficulty(currentuser:str=Depends(get_current_user)):
    res=get_difficulty_stats(currentuser)
    return res

@app.get('/count_by_topic')
def count_by_topic(currentuser:str=Depends(get_current_user)):
    data=get_topic_stats(currentuser)
    return data

@app.get('/activedates')
def user_active(currentuser:str=Depends(get_current_user)):
    return get_active_dates(currentuser)
