from src.pkg.user.model.user import User
from src.pkg.authentication.helper import helper

class UserService:
    def __init__(self, user_store):
        self.user_store = user_store

    def create_user(self, user: User) -> User:
        hash = helper.hash_password(user.password)
        user.password = hash

        return self.user_store.create_user(user)
    
    def get_user(self, id: int, keep_sensitive_filelds: bool = False) -> User:
        user = self.user_store.get_user(id)
        
        if not keep_sensitive_filelds:
            user.drop_sensitive_fields()

        return user