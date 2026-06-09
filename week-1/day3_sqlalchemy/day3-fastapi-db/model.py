from sqlalchemy import column,String,Integer,Column,Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Customer(Base):
    __tablename__="customers"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    age=Column(Integer)
    city=Column(String)


