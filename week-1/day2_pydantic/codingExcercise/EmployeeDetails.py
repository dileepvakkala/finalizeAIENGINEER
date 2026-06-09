from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()
emps=[]
class Employee(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt= 18)
    salary: float =Field(gt= 0)

@app.post("/emp")
def createEmployee(emp: Employee):
    emps.append(emp)
    return "employee added successfully"

@app.get("/emp1")
def getEmployeeDetails():
    return emps





