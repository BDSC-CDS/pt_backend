import traceback

from server_template.models import TemplatebackendUser
from server_template.models import TemplatebackendCreateUserReply
from server_template.models import TemplatebackendCreateUserResult
from server_template.models import TemplatebackendGetUserReply
from server_template.models import TemplatebackendGetUserResult
from server_template.models import TemplatebackendUpdatePasswordRequest

import src.internal.api.controllers.converter.user as user_converter
from src.pkg.user.service.user import UserService

class UsersController():
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def user_service_create_user(self, user, body: TemplatebackendUser):
        u = user_converter.user_to_business(body)
        try:
            user = self.user_service.create_user(u)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        return TemplatebackendCreateUserReply(TemplatebackendCreateUserResult(id=user.id))

    def user_service_delete_user(self, user, id: int):
        return "Not implemented", 501


    def user_service_get_user(self, user, id: int):
        try:
            user = self.user_service.get_user(by='id', identifier=id)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if user is None:
            return TemplatebackendGetUserReply(TemplatebackendGetUserResult(user=None)), 404

        user = user_converter.user_from_business(user)

        return TemplatebackendGetUserReply(TemplatebackendGetUserResult(user=user))


    def user_service_get_user_me(self, user):
        return "Not implemented", 501


    def user_service_reset_password(self, user, id: int, body: object):
        return "Not implemented", 501


    def user_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        return "Not implemented", 501
