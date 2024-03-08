from server_template.models import TemplatebackendUser
from server_template.models import TemplatebackendUpdatePasswordRequest
from src.internal.api.controllers.user_controller import UsersController
from src.internal.util.interface.implements import implements_interface
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService

class UsersControllerAudit():
    def __init__(self, next: UsersController):
        self.next = next
        implements_interface(UsersController, UsersControllerAudit)

    def user_service_create_user(self, user, body: TemplatebackendUser):
        AuditLogService.log_event(AuditLog(user,"created user"))
        return self.next.user_service_create_user(user, body)

    def user_service_delete_user(self, user, id: int):
        AuditLogService.log_event(AuditLog(user,"deleted user of id "+id))
        return self.next.user_service_delete_user(user, id)

    def user_service_get_user(self, user, id: int):
        AuditLogService.log_event(AuditLog(user,"accessed user of id "+id))
        return self.next.user_service_get_user(user, id)

    def user_service_get_user_me(self, user):
        AuditLogService.log_event(AuditLog(user,"accessed user of id "+id))
        return self.next.user_service_get_user_me(user)

    def user_service_reset_password(self, user, id: int, body: object):
        AuditLogService.log_event(AuditLog(user,"reset password "))
        return self.next.user_service_reset_password(user, id, body)

    def user_service_update_password(self, user, body: TemplatebackendUpdatePasswordRequest):
        AuditLogService.log_event(AuditLog(user,"updated password "))
        return self.next.user_service_update_password(user, body)
