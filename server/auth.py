import bcrypt
import jwt
from datetime import datetime, timedelta, timezone

# security
SECRET_KEY = "my_super_secret_key_change_me"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


# hasing
# encode utf-8 = turns text to byte, gensalt= add 2 random chars before hash,decode utf-8 = turn back byte to text


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


# check password typed vs hased password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


# CREATE JWT FOR LOGIN USER
def create_access_token(user_id: int, email: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)

    payload = {"sub": str(user_id), "email": email, "exp": expire}

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token
