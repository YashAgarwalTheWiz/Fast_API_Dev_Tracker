from fastapi import APIRouter
from models import user,login_user as verify_user
from repository.user_repository import login_user_dao
from auth_utils import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from services.user_service import register_user as register_user_service,login_user_service

router = APIRouter()

@router.post('/register')
def register_user(user:user):
    return register_user_service(user)

@router.post('/login')
def login_user(user:verify_user):
    return login_user_service(user)

@router.post('/token')
def swagger_login(form_data: OAuth2PasswordRequestForm = Depends()):
    from models import login_user
    user = login_user(email=form_data.username, password=form_data.password)
    data = login_user_dao(user)
    if data:
        token = create_access_token({"sub": form_data.username})
        return {'access_token': token, 'token_type': 'bearer'}
    return None