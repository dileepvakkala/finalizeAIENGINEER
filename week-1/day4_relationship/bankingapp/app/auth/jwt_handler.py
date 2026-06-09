from jose import jwt
from datetime import datetime
from datetime import timedelta

SECRET_KEY = "banking-secret"

ALGORITHM = "HS256"


def create_access_token(username):

    expire = (
            datetime.utcnow()
            + timedelta(minutes=30)
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )