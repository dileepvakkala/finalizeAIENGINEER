from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db

from schemas.accountSchema import AccountCreate
from service.accountService import AccountService

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post("/")
def create_account(
        account: AccountCreate,
        db: Session = Depends(get_db)
):

    return AccountService.create_account(
        db,
        account
    )


@router.get("/")
def get_accounts(
        db: Session = Depends(get_db)
):

    return AccountService.get_accounts(db)