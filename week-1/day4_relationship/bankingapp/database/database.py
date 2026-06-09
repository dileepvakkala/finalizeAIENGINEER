from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DATABASE_URL
from sqlalchemy.orm import declarative_base
Base=declarative_base()
import logging
import logging
logging.basicConfig(
    level= logging.INFO
)
logger= logging.getLogger("CustomerService")
logger.info("Creating database tables if they do not exist"+str(DATABASE_URL))
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()