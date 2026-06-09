from passlib.context import CryptContext

# Using argon2 instead of bcrypt to avoid 72-byte password limitation
_pwd_context = None

def get_pwd_context():
    global _pwd_context
    if _pwd_context is None:
        _pwd_context = CryptContext(
            schemes=["argon2"],
            deprecated="auto"
        )
    return _pwd_context


def hash_password(password):
    # Argon2 doesn't have the 72-byte limitation, but we still handle it safely
    return get_pwd_context().hash(password)


def verify_password(
        plain_password,
        hashed_password
):
    return get_pwd_context().verify(
        plain_password,
        hashed_password
    )