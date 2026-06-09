from fastapi import FastAPI
from pydantic_core.core_schema import CustomErrorSchema

from schema import CustomerCreate
from model import Base
app = FastAPI()
Base.metadata.create_all(bind=engine)
@app.post("/customers")
def create_customer(customer: CustomerCreate):
    return {"message":"Customer created successfully"}
