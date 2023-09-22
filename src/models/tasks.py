import datetime
from sqlalchemy import Column, Integer, String, bool
from typing import Optional
from config.database import BASE
 
    
class Task(BASE):
    __tablename__ = 'tasks'
    id: Optional[int] = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, unique=True)
    description: str = Column(String)
    due_date: datetime = Column(datetime, index=True)
    status: str = Column(bool, default=False, index=True)
    created_at: datetime = datetime.datetime.now()