
from sqlalchemy import Column, String, Date, Integer, ForeignKey

from ..common.base import Base


class List(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True)
    tasks = relationship('Task')


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column('title', String(32))
    completed = Column('completed', Boolean)
    due_date = Column('due_date', Date)
    list_id = Column(Integer, ForeignKey('lists.id'))