from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from database.database import Base

class Customer(Base):

    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    city = Column(String)

    accounts = relationship(
        "Account",
        back_populates="customer",
        cascade="all, delete"
    )