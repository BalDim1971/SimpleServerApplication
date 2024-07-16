import uvicorn

from sqlalchemy.orm import Session
from typing import Union, Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# app.include_router(api_auth)
# app.include_router(api_users)
#
#
# @app.get('/')
# async def read_root(db: Session = Depends(get_db)):
#     return {"message": "Welcome to FastAPI authentication and authorization example"}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

if __name__ == '__main__':
    # uvicorn.run(app, host=DB_HOST, port=DB_PORT)
    uvicorn.run(app)
