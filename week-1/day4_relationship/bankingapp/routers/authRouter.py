from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from database.database import get_db
from auth.password_handler import hash_password
from schemas.users import UserCreate, LoginRequest
from model.users import User
from auth.jwt_handler import create_access_token
from auth.password_handler import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.post("/register")
def register(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    hashed_password = hash_password(
        user.password
    )

    user_db = User(
        username=user.username,
        password=hashed_password,
        role="USER"
    )

    db.add(user_db)
    db.commit()

    return {
        "message":
            "User Created Successfully"
    }

@router.post("/login")
def login(
        request: LoginRequest,
        db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username ==
        request.username
    ).first()

    if not user:

        raise HTTPException(
            401,
            "Invalid Username"
        )

    valid = verify_password(
        request.password,
        user.password
    )

    if not valid:

        raise HTTPException(
            401,
            "Invalid Password"
        )

    token = create_access_token(
        user.username
    )

    return {
        "access_token": token
    }