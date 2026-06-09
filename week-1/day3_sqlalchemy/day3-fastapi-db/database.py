from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



DATABASE_URL = (
    "postgresql://postgres:root@5052/bankdb"
)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)