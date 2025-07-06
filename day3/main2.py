from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

dummydb = {
    1: "Work",
    2: "Gym",
    3: "sleep"
}

class todoModel(BaseModel):
    todo : str = Field(max_length=5)

def indexValidator(index: int):
    if index not in dummydb.keys():
        raise HTTPException(status_code=404, detail="Invalid index")
    return index

indValDI = Annotated[int, Depends(indexValidator)]

@app.get("/all")
def get_all_todo():
    return dummydb

@app.get("/all/{index}")
def get_todo(index: indValDI):
    return{
        index: dummydb[index]
    }

@app.post("/create")
def create_todo(todo: todoModel):
    index = max(dummydb.keys(), default=0)+1
    dummydb[index]= todo.todo
    # return{
    #     "todo": dummydb
    # }

@app.put("/edit/{index}")
def edit_todo(index: indValDI, todo: todoModel):
    dummydb[index] = todo.todo
    return{
        "todo": dummydb
    }

@app.delete("/delete/{index}")
def delete_todo(index: indValDI):
    del_item = dummydb.pop(index)
    return{
        "message" : f"Deleted successfully id: {index}"
    }
