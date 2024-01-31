from server_template.models import TemplatebackendUser
from server_template.models import TemplatebackendUpdatePasswordRequest
from src.internal.api.controllers.user_controller import UsersController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class UsersControllerAuthentication():
    def __init__(self, next: UsersController):
        self.next = next
        implements_interface(UsersController, UsersControllerAuthentication)

    def user_service_create_user(self, user, body: TemplatebackendUser):
        return self.next(user, body)

    def user_service_delete_user(self, user, id: int):
        if not is_admin_or_self(user, id):
            return None, 403

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
        if not is_admin_or_self(user, id):
            return None, 403

        return self.next(user, id, body)

    def user_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        if not is_authenticated(user):
            return None, 403
        
        return self.next(user, body)