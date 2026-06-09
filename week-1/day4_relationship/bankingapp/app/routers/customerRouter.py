from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db

from schemas.customerSchema import CustomerCreate
from service.customerService import CustomerService

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/")
def create_customer(
        customer: CustomerCreate,
        db: Session = Depends(get_db)
):

    return CustomerService.create_customer(
        db,
        customer
    )

@router.put("/{customer_id}")
def update_customer(customer_id: int ,customer: CustomerCreate,db: Session = Depends(get_db)):
    return CustomerService.update_customer(db,customer_id,customer)
@router.get("/")
def get_customers(
        db: Session = Depends(get_db)
):

    return CustomerService.get_customers(db)