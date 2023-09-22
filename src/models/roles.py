from sqlalchemy import Column, Integer, String
from typing import Optional
from config.database import BASE


class Role(BASE):
    __tablename__ = 'roles'
    id: Optional[int] = Column(Integer, primary_key=True, index=True)
    tag: str = Column(String, unique=True, index=True)