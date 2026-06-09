from pydantic import BaseModel

class CustomerCreate(BaseModel):

    name: str
    age: int
    city: str