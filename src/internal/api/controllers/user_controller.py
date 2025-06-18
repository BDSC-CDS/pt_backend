import traceback

from server_template.models import TemplatebackendUser
from server_template.models import TemplatebackendCreateUserReply
from server_template.models import TemplatebackendCreateUserResult
from server_template.models import TemplatebackendGetUserReply
from server_template.models import TemplatebackendGetUserResult
from server_template.models import TemplatebackendGetUserMeReply
from server_template.models import TemplatebackendGetUserMeResult
from server_template.models import TemplatebackendUpdatePasswordRequest
from server_template.models import TemplatebackendSearchUsersRequest
from server_template.models import TemplatebackendSearchUsersReply

import src.internal.api.controllers.converter.user as user_converter
from src.pkg.user.service.user import UserService

class UsersServiceController():
    def __init__(self, config, users_service: UserService):
        self.users_service = users_service
        self.config = config

    def users_service_create_user(self, user, body: TemplatebackendUser):
        u = user_converter.user_to_business(body)
        try:
            user = self.users_service.create_user(u)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        return TemplatebackendCreateUserReply(TemplatebackendCreateUserResult(id=user.id))

    def users_service_delete_user(self, user, id: int):
        return "Not implemented", 501


    def users_service_get_user(self, user, id: int):
        try:
            user = self.users_service.get_user(by='id', identifier=id)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if user is None:
            return TemplatebackendGetUserReply(TemplatebackendGetUserResult(user=None)), 404

        user = user_converter.user_from_business(user)

        return TemplatebackendGetUserReply(TemplatebackendGetUserResult(user=user))


    def users_service_get_user_me(self, user):
        try:
            user = self.users_service.get_user(by='id', identifier=user.id)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if user is None:
            return TemplatebackendGetUserMeReply(TemplatebackendGetUserMeResult(me=None)), 404

        user = user_converter.user_from_business(user)

        return TemplatebackendGetUserMeReply(TemplatebackendGetUserMeResult(me=user))


    def users_service_reset_password(self, user, id: int, body: object):
        return "Not implemented", 501


    def users_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        return "Not implemented", 501

    def users_service_search_users(self, user, body: TemplatebackendSearchUsersRequest):
        if not self.config.services.users_service.allow_searching_user_by_mail:
            return "Not found", 404
        
        try:
            users = self.users_service.search_users(user.tenantid, body.email_like)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        
        users = [user_converter.user_email_from_business(u) for u in users]

        return TemplatebackendSearchUsersReply(users)