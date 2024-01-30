from server_template.models.templatebackend_user import TemplatebackendUser
from server_template.models.templatebackend_update_password_request import TemplatebackendUpdatePasswordRequest
from src.internal.api.controllers.user_controller import UsersController
from src.pkg.user.model.user import Role
from src.internal.util.interface.implements import implements_interface

def is_admin(user):
    return is_authenticated(user) and Role("admin") in user.roles

def is_authenticated(user):
    return user is not None

class UsersControllerAuthentication():
    def __init__(self, next: UsersController):
        self.next = next
        implements_interface(UsersController, UsersControllerAuthentication)

    def user_service_create_user(self, user, body: TemplatebackendUser):
        return self.next(user, body)

    def user_service_delete_user(self, user, id: int):
        return self.next(user, id)

    def user_service_get_user(self, user, id: int):
        if not is_admin(user):
            return None, 403
        return self.next(user, id)

    def user_service_get_user_me(self, user):
        if not is_authenticated(user):
            return None, 403
        return self.next(user)

    def user_service_reset_password(self, user, id: int, body: object):
        return self.next(user, id, body)

    def user_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        return self.next(user, body)