from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy_utils import PasswordType, EmailType
from database import Base

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    todo_name = Column(String)
    todo_body = Column(String)
    created = Column(DateTime(timezone=True), server_default=func.now())
    deadline = Column(DateTime(timezone=True), onupdate=func.now())
    
    
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    fullname = Column(String)
    email = Column(EmailType)
    password = Column(PasswordType)
    
    