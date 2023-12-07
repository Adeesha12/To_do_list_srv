from  pydantic import BaseModel, Field, EmailStr
from datetime import date
 


class Todo(BaseModel):
    # todo_id: int = Field(default=None)
    todo_name: str = Field(default=None)
    todo_body: str = Field(default=None)
    created: date = Field(default=None)
    deadline: date = Field(default=None)
  
  
class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None, min_length=6, max_length=12)
    class Config:
        the_schema ={
            "User_demo" : {
                "name":"Bob",
                "email":"Bob@eaxample.com",
                "password":"123@4"
            }
        }
          
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None, min_length=6, max_length=12)
    class Config:
        the_schema ={
            "User_demo" : {
                "email":"Bob@eaxample.com",
                "password":"123@4"
            }
        }