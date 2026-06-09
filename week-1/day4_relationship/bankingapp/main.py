from fastapi import FastAPI

from database.database import engine
from database.database import Base

from routers.customerRouter import router as customer_router
from routers.accountRouter import router as account_router
from routers.authRouter import router as auth_router
from model.customer import Customer
from model.account import Account

app = FastAPI(
    title="Banking Application"
)

Base.metadata.create_all(bind=engine)

app.include_router(customer_router)
app.include_router(account_router)
app.include_router(auth_router)


@app.get("/")
def home():

    return {
        "message": "Banking Application Running"
    }