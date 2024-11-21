from fastapi import APIRouter, Path
from model import Todo

todo_list = []

todo = APIRouter()

@todo.post("/todo")
def add_todo(todo:dict):
    todo_list.append(todo)
    return {"message":"Added"}

@todo.get("/todo")
def show_todos():
    return {"todos":todo_list}

@todo.get("/todo/{todo_id}")
def  show_one_todo(todo_id: int=Path(...,title="ID")):
    for todo in todo_list:
        if todo["id"] == todo_id:
            return { "todo":todo }
    return {"message": "ID doesn't exist"}