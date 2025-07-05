from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

todoList = ["work", "seep", "gym"]

class Toto(BaseModel):
    todo: str

def index_validator(index:int):
    if index < 0 or index>=len(todoList):
        raise HTTPException(status_code=404,detail="Invalid index")
    return index

todoDI = Annotated[int, Depends(index_validator)]

@app.get("/mytodo/{index}")
def get_todo_a(index: todoDI):
    return{
        index: todoList[index]
    }

@app.get("/todo/{index}")
def get_todo(
    index: int = Depends(index_validator)
    ):
    return{
        index: todoList[index]
    }

