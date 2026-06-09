from pydantic import BaseModel


class CustomerCreate(BaseModel):

    name: str
    city: str


class CustomerResponse(BaseModel):

    id: int
    name: str
    city: str

    class Config:
        from_attributes = True