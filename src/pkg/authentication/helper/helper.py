
import bcrypt

def hash_password(password: str):
    password_bytes = str.encode(password)
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")

def is_password_correct(password: str, hashed: str) -> bool:
    password_bytes = str.encode(password)
    hashed_bytes = str.encode(hashed)

    return bcrypt.checkpw(password_bytes, hashed_bytes)
