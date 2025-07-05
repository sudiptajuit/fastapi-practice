from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    todo: str

todolist = []

@app.post("/create")
async def create_todo(todo: Todo):
    todolist.append(todo)
    return{
        "current todo": todolist
    }

@app.get("/mytodo/{index}")
async def get_todo(index: int):
    print(len(todolist))
    if index<0 or index>=len(todolist):
        return{
            "message" : "Invalid todo"
        }
    else:
        return{
            f"Index -> {index}" : todolist[index]
        }

@app.put("/edit/{index}")
async def edit_todo(index: int, todo: Todo):
    if index<0 or index>=len(todolist):
        return{
            "message" : "Invalid todo"
        }
    else:
        todolist[index]= todo
        return{
            f"edited at {index}": todo
        }
    
@app.delete("/delete/{index}")
async def delete_todo(index: int):
    if index<0 or index>=len(todolist):
        return{
            "message" : "Invalid todo"
        }
    else:
        d_item = todolist.pop(index)
        return{
            "deleted": {d_item}
        }