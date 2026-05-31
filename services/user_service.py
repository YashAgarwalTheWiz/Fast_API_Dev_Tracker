from repository.user_repository import insert_user,login_user_dao
from models import user,login_user
from fastapi import HTTPException
from auth_utils import create_access_token

def register_user(user:user):
    data=insert_user(user)
    if data=='success':
        return {"message": "registered successfully"}
    else:
        raise HTTPException(status_code=400,detail='Email aldready exists')
    
def login_user_service(user:login_user):
    data=login_user_dao(user)
    if data :
        token=create_access_token({"sub": user.email})
        return {'access_token':token}
    raise HTTPException(status_code=401,detail='Invalid email or password')