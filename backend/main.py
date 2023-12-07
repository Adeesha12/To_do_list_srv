from fastapi import FastAPI
import uvicorn

from schema import Todo
import model
from database import engine
from routes.todos import todo_router
from routes.auth import register_router


model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router)
app.include_router(register_router)



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=4,reload=True)

