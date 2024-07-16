from sqlalchemy import Column, String
from pydantic import BaseModel


class Token(BaseModel):
    access_token = Column(String)
    token_type = Column(String)


class TokenData(BaseModel):
    username = Column(String, default=None)
