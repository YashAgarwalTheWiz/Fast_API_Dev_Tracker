from fastapi import APIRouter
from models import user,login_user as verify_user
from dao import insert_user,login_user_dao
from auth_utils import create_access_token

router = APIRouter()

@router.post('/register')
def register_user(user:user):
    return insert_user(user)

@router.post('/login')
def login_user(user:verify_user):
    data=login_user_dao(user)
    if data :
        token=create_access_token({"sub": user.email})
        return {'access_token':token}
    return None
    