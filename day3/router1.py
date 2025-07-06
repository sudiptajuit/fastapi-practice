from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated

router = APIRouter(prefix="/todo", tags=["todolist"])

todoList = {
    1: 'gym',
    2: 'sleep',
    3: 'work',
}

class todoModel(BaseModel):
    todo : str

def validateId(id: int):
    if id not in todoList.keys():
        raise HTTPException(status_code=404, detail="Invalid index")
    return id

valIndexDI = Annotated[int, Depends(validateId)]

@router.get("/all")
def get_all():
    return{
        "todolist" : todoList
    }

@router.get("/index/{id}")
def get_index_todo(id: valIndexDI):
    return{
        todoList.get(id)
    }

@router.post("/add")
def add_todo(todo: todoModel):
    id = max(todoList.keys(), default=0)+1
    todoList[id] = todo.todo
    return{
        "todolist" : todoList
    }

@router.put("/edit")
def edit_router(id: valIndexDI, todo: todoModel):
    todoList[id] = todo.todo
    return{
        "todoList" : todoList
    }

@router.delete("/delete/{id}")
def delete_todo(id: valIndexDI):
    delete_item = todoList.pop(id)
    return{
        "deleted item": delete_item
    }



