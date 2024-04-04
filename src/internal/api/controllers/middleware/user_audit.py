from server_template.models import TemplatebackendUser
from server_template.models import TemplatebackendUpdatePasswordRequest
from src.internal.api.controllers.user_controller import UsersController
from src.internal.util.interface.implements import implements_interface
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService

class UsersControllerAudit():
    def __init__(self, next: UsersController,auditLogService: AuditLogService):
        self.next = next
        self.auditLogService = auditLogService
        implements_interface(UsersController, UsersControllerAudit)

    def user_service_create_user(self, user, body: TemplatebackendUser):
        body_serialized = f"id: {body.id or ''}, first_name: {body.first_name or ''}, last_name: {body.last_name or ''}, username: {body.username or ''}, email: {body.email or ''}"
        try:
            response =  self.next.user_service_create_user(user, body)
            self.auditLogService.log_event(AuditLog(service="user", userid=body.id,action="created user",body=body_serialized,response=response))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=body.id,action="Error creating user",body=body_serialized,response=response, error=True))
            raise e

    def user_service_delete_user(self, user, id: int):
        try:
            response =  self.next.user_service_delete_user(user, id)
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="deleted user of id "+str(id), response=response))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="Error deleting user of id "+ str(id), response=response, error=True))
            raise e


    def user_service_get_user(self, user, id: int):
        try:
            response =  self.next.user_service_get_user(user, id)
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="accessed user of id "+str(id), response=response))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="Error accessing user of id "+str(id), response=response, error=True))
            raise e


    def user_service_get_user_me(self, user):
        try:
            response = self.next.user_service_get_user_me(user)
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="accessed user of id "+user, response=response))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="Error accessing user of id "+user, response=response, error=True))
            raise e


    def user_service_reset_password(self, user, id: int, body: object):
        try:
            response =  self.next.user_service_reset_password(user, id, body)
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="reset password"))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="Error resetting password",error=True))
            raise e


    def user_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        try:
            response = self.next.user_service_update_password(user, body)
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="updated password"))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="user", userid=user,action="Error updating password",error=True))
            raise e
