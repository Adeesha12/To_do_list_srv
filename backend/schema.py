from  pydantic import BaseModel, Field
from datetime import date
 


class Todo(BaseModel):
    todo_id: int = Field(default=None)
    todo_name: str = Field(default=None)
    todo_body: str = Field(default=None)
    created: date = Field(default=None)
    deadline: date = Field(default=None)
    