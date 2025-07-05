from fastapi import (
    FastAPI, 
    APIRouter, 
    Depends,
    HTTPException,
    )
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Server is running!"}

router1 = APIRouter(prefix="/details", tags=["Details"])
router2 = APIRouter(prefix="/edit", tags=["Edit"])

todoList = ["sleep", "work", "gym", "lunch"]

class dataModel(BaseModel):
    todo : str

def indexValidator(index: int):
    if index<0 or index>=len(todoList):
        raise HTTPException(status_code=404, detail="Invalid index")
    return index
    
indexValDI = Annotated[int, Depends(indexValidator)]

@router1.post("/create")
def create_todo(todo: dataModel):
    todoList.append(todo.todo)
    return{
        "Created todo": todoList
    }

@router1.get("/all")
def get_todo():
    return{
        "My todo": todoList
    }

@router1.get("/all/{index}")
def get_todo_index(index: indexValDI):
    return{
        "My todo": todoList[index]
    }

@router2.put("/edit")
def edit_todo(index: indexValDI, todo:dataModel):
    todoList[index] = todo.todo
    return{
        index : todoList[index]
    }

@router2.delete("/delete")
def delete_todo(index: indexValDI):
    deleted_item = todoList.pop(index)
    return{
        "Deleted Todo": deleted_item
    }

app.include_router(router1)
app.include_router(router2)