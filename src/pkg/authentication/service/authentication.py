import jwt
from datetime import datetime, timedelta

from src.pkg.user.model.user import User
from src.pkg.authentication.helper import helper

def user_to_jwt_payload(user: User, expiration_time: int) -> dict:

    # Prepare the JWT payload
    jwt_payload = {
        "sub": str(user.id), 
        "email": user.email,
        "tenantid": user.tenantid,
        "roles": user.roles,
        "username": user.username,
        "iat": datetime.utcnow(),  # Issued At
        "exp": datetime.utcnow() + timedelta(seconds=expiration_time)  # Expiration Time, set to 1 hour from now
    }

    return jwt_payload

class AuthenticationService:
    def __init__(self, config, user_service):
        self.config = config
        self.user_service = user_service

    def authenticate(self, username:str, password:str) -> str:
        user = self.user_service.get_user(by="username", identifier=username, keep_sensitive_filelds=True)
        correct = helper.is_password_correct(password, user.password)

        if not correct:
            return ""

        payload = user_to_jwt_payload(user, self.config.daemon.jwt.expiration_time)
        token = jwt.encode(payload, self.config.daemon.jwt.secret, algorithm="HS256")

        return token
