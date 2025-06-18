import jwt
from datetime import datetime, timedelta

from src.pkg.user.model.user import User
from src.pkg.authentication.helper import helper

def user_to_jwt_payload(user: User, expiration_time: int) -> dict:

    # Prepare the JWT payload
    jwt_payload = {
        "sub": str(user.id) if user.id else None, 
        "email": user.email,
        "tenantid": user.tenantid,
        "roles": user.to_dict()["roles"],
        "username": user.username,
        "iat": datetime.utcnow(),  # Issued At
        "exp": datetime.utcnow() + timedelta(seconds=expiration_time)  # Expiration Time, set to 1 hour from now
    }

    return jwt_payload

def user_to_token(user: User, expiration_time: int, secret: str) -> str:
    payload = user_to_jwt_payload(user, expiration_time)
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

class AuthenticationService:
    def __init__(self, config, users_service):
        self.config = config
        self.users_service = users_service

    def authenticate(self, username:str, password:str) -> str:
        user = self.users_service.get_user(by="username", identifier=username, keep_sensitive_filelds=True)
        if user is None:
            return ""
        
        correct = helper.is_password_correct(password, user.password)

        if not correct:
            return ""

        return self.user_to_token(user)
    
    def userid_to_token(self, userid: int) -> str:
        user = self.users_service.get_user(by="id", identifier=userid, keep_sensitive_filelds=True)
        if user is None:
            return ""
        
        return self.user_to_token(user)
    
    def user_to_token(self, user: User) -> str:
        expiration_time = self.config.daemon.jwt.expiration_time
        secret = self.config.daemon.jwt.secret
        token = user_to_token(user, expiration_time, secret)

        return token
    
    def token_to_user(self, api_key):
        token = jwt.decode(api_key, self.config.daemon.jwt.secret, algorithms=["HS256"])

        user_id = token['sub']
        user = None
        if user_id is not None:
            user = self.users_service.get_user(by='id', identifier=user_id)


        if user is not None:
            return user

        if token.get('user') is not None:
            u = token.get("user")
            user = User.from_dict(u)
            return user

        return None