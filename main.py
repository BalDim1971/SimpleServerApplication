import uvicorn

from sqlalchemy.orm import Session, joinedload
from fastapi import FastAPI, Depends

from auth.routes import api_auth as auth_router
from src.config import DB_HOST, DB_PORT
from users.routes import api_users as users_router

from src.services import create_db
from src.database import Base, engine, get_db

create_db()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Простой сервер с авторизацией",
)

app.include_router(auth_router)
app.include_router(users_router)


@app.get('/')
def read_root(db: Session = Depends(get_db)):
    return {"message": "Welcome to FastAPI authentication and authorization example"}


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host=DB_HOST, port=DB_PORT)
