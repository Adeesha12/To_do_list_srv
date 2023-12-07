from fastapi import APIRouter, Body, HTTPException, Depends
from schema import  UserSchema, UserLoginSchema
from auth.jwt_handler import sign_jwt
from database import get_db
from typing import List, Annotated
from sqlalchemy.orm import Session
import model

register_router = APIRouter(
    prefix="/v1/register",
    tags=["register"]
)


db_dependancy = Annotated[Session, Depends(get_db)]

@register_router.post("/user/signup")
def user_signup(db:db_dependancy, user:UserSchema = Body(default=None)) -> dict:
    db_user = model.Users(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return sign_jwt(user.email)


@register_router.post("/user/login")
def user_signup(db:db_dependancy, user:UserLoginSchema = Body()) -> dict:
    if check_user(user,db):
        return sign_jwt(user.email)
    else:
        return {
            "error" : "invalid login details !"
        }
        
        
def check_user(data: UserLoginSchema,db:db_dependancy):
    return True if db.query(data).filter(model.Users.email==data.email,
                                         model.Users.password==data.password).one() else False
