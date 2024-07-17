from fastapi import APIRouter, Depends
from auth.services import get_current_user
from users.schema import User
from users.model import User as UserModel

api_users = APIRouter(tags=['users'], prefix='/users')


@api_users.get("/me", response_model=User)
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user
