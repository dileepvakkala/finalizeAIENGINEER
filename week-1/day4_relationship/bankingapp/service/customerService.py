from repositories.customerRepository import CustomerRepository
import logging
logging.basicConfig(
    level= logging.INFO
)
logger= logging.getLogger("CustomerService")
class CustomerService:


    @staticmethod
    def create_customer(db, customer):

        return CustomerRepository.create(
            db,
            customer
        )

    @staticmethod
    def get_customers(db):
        logger.info("Fetching all customers from the database")
        return CustomerRepository.get_all(db)

    @staticmethod
    def update_customer(db,customer_id,customer):

        return CustomerRepository.updateCustomer(
            db,
            customer_id,
            customer
        )

    @staticmethod
    def delete_customer(db,customer_id):
        return CustomerRepository.deleteCustomer(
            db,
            customer_id
        )