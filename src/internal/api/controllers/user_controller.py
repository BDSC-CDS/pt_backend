import connexion
import traceback
from typing import Dict
from typing import Tuple
from typing import Union
from inspect import getmembers, isfunction


from server_template.models.rpc_status import RpcStatus
from server_template.models.templatebackend_user import TemplatebackendUser
from server_template.models.templatebackend_create_user_reply import TemplatebackendCreateUserReply
from server_template.models.templatebackend_create_user_result import TemplatebackendCreateUserResult
from server_template.models.templatebackend_get_user_reply import TemplatebackendGetUserReply
from server_template.models.templatebackend_get_user_result import TemplatebackendGetUserResult
# from server_template.models.templatebackend_ import 
# from server_template.models.templatebackend_ import 
from server_template.models.templatebackend_update_password_request import TemplatebackendUpdatePasswordRequest
from server_template import util

import src.internal.api.controllers.converter.user as user_converter
from src.pkg.user.service.user import UserService

class UsersController():
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def user_service_create_user(self, body: TemplatebackendUser):
        u = user_converter.user_to_business(body)
        try:
            user = self.user_service.create_user(u)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        
        print("user", user)

        return TemplatebackendCreateUserReply(TemplatebackendCreateUserResult(id=user.id))

    def user_service_delete_user(self, id: int):
        """Delete a user

        This endpoint deletes a user

        :param id: 
        :type id: int

        :rtype: Union[TemplatebackendDeleteUserReply, Tuple[TemplatebackendDeleteUserReply, int], Tuple[TemplatebackendDeleteUserReply, int, Dict[str, str]]
        """

        return "Not implemented", 501


    def user_service_get_user(self, id: int):
        """Get a user

        This endpoint returns a user

        :param id: 
        :type id: int

        :rtype: Union[TemplatebackendGetUserReply, Tuple[TemplatebackendGetUserReply, int], Tuple[TemplatebackendGetUserReply, int, Dict[str, str]]
        """

        print("id", id)


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


    def user_service_get_user_me(self):
        """Get my own user

        This endpoint returns the details of the authenticated user


        :rtype: Union[TemplatebackendGetUserMeReply, Tuple[TemplatebackendGetUserMeReply, int], Tuple[TemplatebackendGetUserMeReply, int, Dict[str, str]]
        """

        return "Not implemented", 501


    def user_service_reset_password(self, id: int, body: object):
        """Reset password

        This endpoint resets a user&#39;s password

        :param id: 
        :type id: int
        :param body: 
        :type body: 

        :rtype: Union[TemplatebackendResetPasswordReply, Tuple[TemplatebackendResetPasswordReply, int], Tuple[TemplatebackendResetPasswordReply, int, Dict[str, str]]
        """

        return "Not implemented", 501


    def user_service_update_password(self, body: TemplatebackendUpdatePasswordRequest):
        """Update password

        This endpoint updates the password of the authenticated user

        :param body: 
        :type body: dict | bytes

        :rtype: Union[TemplatebackendUpdatePasswordReply, Tuple[TemplatebackendUpdatePasswordReply, int], Tuple[TemplatebackendUpdatePasswordReply, int, Dict[str, str]]
        """
        # if connexion.request.is_json:
        #     body = TemplatebackendUpdatePasswordRequest.from_dict(connexion.request.get_json())

        return "Not implemented", 501