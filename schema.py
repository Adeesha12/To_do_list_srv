from  pydentic import BaseModel, Field
from datetime import date
 


class Todo(BaseModel):
    todo_id: int = Field()
    todo_name: str = Field()
    todo_body: str = Field()
    created: date = Field()
    deadline: Optional[date] = Field()
    