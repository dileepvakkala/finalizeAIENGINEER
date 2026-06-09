from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Account(Base):

    __tablename__ = "accounts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    account_number = Column(
        String,
        unique=True
    )

    balance = Column(Integer)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    customer = relationship(
        "Customer",
        back_populates="accounts"
    )