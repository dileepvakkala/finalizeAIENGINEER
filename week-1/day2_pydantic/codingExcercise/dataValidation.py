from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()

class Customer(BaseModel):
    name: str = Field(min_length=3)
    age: int =Field(gt=0)
    email: Optional[str]=None

@app.post("/user")
def customerDetails(customer: Customer):
    return customer
