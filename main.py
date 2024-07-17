from fastapi import FastAPI


from auth.routes import api_auth
from src.config import DB_HOST, DB_PORT
from src.database import engine
from users.model import Base
from users.routes import api_users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Простой сервер с авторизацией",
)

app.include_router(api_auth)
app.include_router(api_users)


@app.get('/')
async def read_root():
    return {"message": "Добро пожаловать на простой сервер авторизации"}


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=DB_HOST,
        port=DB_PORT,
        log_level="info",
        reload=True)
