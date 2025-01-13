from src.pkg.user.model.user import User
from src.pkg.authentication.helper import helper

class UserService:
    def __init__(self, user_store):
        self.user_store = user_store

    def create_user(self, user: User) -> User:
        hash = helper.hash_password(user.password)
        user.password = hash

        return self.user_store.create_user(user)

    def get_user(self, by: str, identifier: str | int, keep_sensitive_filelds: bool = False) -> User:
        user = self.user_store.get_user(by=by, identifier=identifier)

        if user is None:
            return None

        if not keep_sensitive_filelds:
            user.drop_sensitive_fields()

        return user
    
    def set_admin(self, userid: int):
        """Set admin role to given userid."""
        return self.user_store.set_admin(userid)
