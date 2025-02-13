from server_template.models import TemplatebackendUser
from server_template.models import TemplatebackendCreateUserReply
from server_template.models import TemplatebackendUpdatePasswordRequest
from server_template.models import TemplatebackendGetUserReply
from server_template.models import TemplatebackendSearchUsersRequest
from src.internal.api.controllers.user_controller import UsersServiceController
from src.internal.util.interface.implements import implements_interface
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService

class UsersServiceControllerAudit():
    def __init__(self, next: UsersServiceController,auditLogService: AuditLogService):
        self.next = next
        self.auditLogService = auditLogService
        implements_interface(UsersServiceController, UsersServiceControllerAudit)

    def users_service_create_user(self, user, body: TemplatebackendUser):
        body_serialized = f"id: {body.id or ''}, first_name: {body.first_name or ''}, last_name: {body.last_name or ''}, username: {body.username or ''}, email: {body.email or ''}"
        try:
            response : TemplatebackendCreateUserReply =  self.next.users_service_create_user(user, body)
            response_serialized = response.result.id
            self.auditLogService.log_event(AuditLog(service="user", userid=body.id,action="created user",body=body_serialized,response=response_serialized))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=body.id,action="Error creating user",body=body_serialized,response=e, error=True))
            raise e

    def users_service_delete_user(self, user, id: int):
        try:
            response =  self.next.users_service_delete_user(user, id)
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="deleted user of id "+str(id), response=response))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="Error deleting user of id "+ str(id), response=e, error=True))
            raise e


    def users_service_get_user(self, user, id: int):
        try:
            response : TemplatebackendGetUserReply =  self.next.users_service_get_user(user, id)
            user = response.result.user
            response_serialized = f"id: {user.id}, first_name: {user.first_name or ''}, last_name: {user.last_name or ''},  \
                username: {user.username or ''}, email: {user.email or ''}, status: {user.status or ''},  \
                roles: {user.roles or ''}"

            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="accessed user of id "+str(id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="Error accessing user of id "+str(id), response=e, error=True))
            raise e


    def users_service_get_user_me(self, user):
        try:
            response : TemplatebackendGetUserReply = self.next.users_service_get_user_me(user)
            user = response.result.me
            response_serialized = f"id: {user.id}, first_name: {user.first_name or ''}, last_name: {user.last_name or ''},  \
                username: {user.username or ''}, email: {user.email or ''}, status: {user.status or ''},  \
                roles: {user.roles or ''}"
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="accessed user of id "+str(user.id), response=response_serialized))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="Error accessing user of id "+str(user.id), response=e, error=True))
            raise e


    def users_service_reset_password(self, user, id: int, body: object):
        try:
            response =  self.next.users_service_reset_password(user, id, body)
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="reset password"))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="Error resetting password",error=True))
            raise e


    def users_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        try:
            response = self.next.users_service_update_password(user, body)
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="updated password"))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="Error updating password",error=True))
            raise e

    def users_service_search_users(self, user, body: TemplatebackendSearchUsersRequest):
        try:
            response = self.next.users_service_search_users(user, body)
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="searched users"))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user.id,action="Error searching users",error=True))
            raise e