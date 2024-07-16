# from sqlalchemy.orm import Session
from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.security import (OAuth2PasswordBearer, OAuth2PasswordRequestForm,
                              HTTPBasic, HTTPBasicCredentials)
from pydantic import BaseModel

#
# from auth.routes import api_auth
# from src.config import DB_HOST, DB_PORT
# from users.routes import api_users
#
# from src.services import create_db
# from src.database import Base, engine, get_db
#
# create_db()
#
# Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Простой сервер с авторизацией",
)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# app.include_router(api_auth)
# app.include_router(api_users)
#
#
# @app.get('/')
# async def read_root(db: Session = Depends(get_db)):
#     return {"message": "Welcome to FastAPI authentication and authorization example"}


secret_user: str = "newphone"
secret_password: str = "whodis?"

basic: HTTPBasicCredentials = HTTPBasic()


@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if (creds.username == secret_user and creds.password == secret_password):
        return {"username": creds.username, "password": creds.password}
    raise HTTPException(status_code=401, detail='Hey!')


if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app, host=DB_HOST, port=DB_PORT, reload=True)
    uvicorn.run("main:app", reload=True)
