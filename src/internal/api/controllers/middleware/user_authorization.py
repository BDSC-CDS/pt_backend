from server_template.models import TemplatebackendUser
from server_template.models import TemplatebackendUpdatePasswordRequest
from server_template.models import TemplatebackendSearchUsersRequest
from src.internal.api.controllers.user_controller import UsersServiceController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class UsersServiceControllerAuthentication():
    def __init__(self, next: UsersServiceController):
        self.next = next
        implements_interface(UsersServiceControllerAuthentication, UsersServiceController)

    def users_service_create_user(self, user, body: TemplatebackendUser):
        return self.next.users_service_create_user(user, body)

    def users_service_delete_user(self, user, id: int):
        if not is_admin_or_self(user, id):
            return None, 403

        return self.next.users_service_delete_user(user, id)

    def users_service_get_user(self, user, id: int):
        if not is_admin(user):
            return None, 403
        return self.next.users_service_get_user(user, id)

    def users_service_get_user_me(self, user):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.users_service_get_user_me(user)

    def users_service_reset_password(self, user, id: int, body: object):
        if not is_admin_or_self(user, id):
            return None, 403

        return self.next.users_service_reset_password(user, id, body)

    def users_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.users_service_update_password(user, body)
    
    def users_service_search_users(self, user, body: TemplatebackendSearchUsersRequest):
        if not is_authenticated(user):
            return None, 403

        return self.next.users_service_search_users(user, body)