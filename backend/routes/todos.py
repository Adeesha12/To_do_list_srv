from fastapi import APIRouter,Depends, HTTPException
from typing import Annotated, List
from sqlalchemy.orm import Session

from schema import Todo
from database import get_db
from auth.jwt_bearer import JWTBearer
import model


todo_router = APIRouter(
    prefix='/v1/todos',
    tags=['todos']
)
todos = []
db_dependancy = Annotated[Session, Depends(get_db)]

@todo_router.get('/todos', dependencies=[Depends(JWTBearer())], response_model=List[Todo])
def get_all_todos(db:db_dependancy):
    results = db.query(model.Todo).all()
    return results

@todo_router.post('/add_todo',dependencies=[Depends(JWTBearer())], response_model=Todo)
def create_todo(todo:Todo, db:db_dependancy):
    db_todo = model.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    db.close()    
    return db_todo
    
@todo_router.put('/update_todo/{todo_id}', dependencies=[Depends(JWTBearer())], response_model=Todo)
def update_todo(todo_id: int, todo:Todo, db: db_dependancy ):
    db_todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    
    if db_todo is None:
        raise HTTPException(status_code=404, detail='not found')
    
    for field,values in todo.model_dump().items():
        setattr(db_todo, field, values)
    
    db.commit()
    db.refresh(db_todo)    
    return  db_todo

@todo_router.delete('/delete_todo', dependencies=[Depends(JWTBearer())], response_model=Todo)
def delete_todo(todo_id: int, db: db_dependancy):
    db_todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail='not found')
    db.delete(db_todo)
    todos.pop(todo_id)
    return f'{todo_id} removed successfuly'


