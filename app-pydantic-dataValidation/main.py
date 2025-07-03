from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class employeeData(BaseModel):
    name: str
    location: str
    age: int
    salary: float

@app.post("/create_emp")
async def create_employee(employee:employeeData):
    print(employee)
    return{
        "Employee Name": employee.name
    }
