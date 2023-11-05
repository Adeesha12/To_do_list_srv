from fastapi import FastAPI
from schema import Todo

app = FastAPI()

todos = []

@app.get('/todos')
def get_all_todos():
    return todos

@app.post('/addtodos')
def create_todo(todo):
    todos.append(todo)
    return 'add one item'
    
@app.put()
def update_todo(todo_id: int, todo: Todo ):
    todos[todo_id] = todo
    return 'suceesfuly updates '   

@app.delete
def delete_todo(todo_id: int, todo: Todo):
    todos.pop(todo_id)
    return f'{todo_id} removed successfuly'


