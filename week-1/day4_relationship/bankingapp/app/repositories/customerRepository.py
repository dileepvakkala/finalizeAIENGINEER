from model.customer import Customer
from fastapi import HTTPException

class CustomerRepository:

    @staticmethod
    def create(db, customer):

        customer_db = Customer(
            name=customer.name,
            city=customer.city
        )

        db.add(customer_db)
        db.commit()
        db.refresh(customer_db)

        return customer_db

    @staticmethod
    def updateCustomer(db,customer_id,customer1):
        customer=db.query(Customer).filter(Customer.id==customer_id).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")

        customer.name=customer1.name
        customer.city=customer1.city
        db.commit()
        db.refresh(customer)
        return customer

    @staticmethod
    def deleteCustomer(db,customer_id):
         customer=db.query(Customer).filter(Customer.id==customer_id).first()
         if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
         db.delete(customer)
         db.commit()
         db.refresh()
         return customer

    @staticmethod
    def get_all(db):

        return db.query(Customer).all()