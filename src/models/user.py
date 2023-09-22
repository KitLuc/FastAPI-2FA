import datetime
from sqlalchemy import Column, Integer, String
from typing import Optional
from config.database import BASE


class User(BASE):
    __tablename__ = 'users'
    id: Optional[int] = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    email: str = Column(String, unique=True)
    password: str = Column(String)
    created_at: datetime = datetime.datetime.now()