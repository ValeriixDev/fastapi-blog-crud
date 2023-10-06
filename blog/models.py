from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    body = Column(String)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

 
