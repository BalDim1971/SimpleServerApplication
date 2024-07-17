from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

DATABASE_URL = (f'postgresql+psycopg2://'
                f'{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
