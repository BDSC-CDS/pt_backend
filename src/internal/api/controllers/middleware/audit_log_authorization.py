from src.internal.api.controllers.audit_log_controller import AuditLogServiceController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class AuditLogServiceControllerAuthentication:
    def __init__(self, next: AuditLogServiceController):
        self.next = next
        implements_interface(AuditLogServiceController, AuditLogServiceControllerAuthentication)

    def audit_log_service_get_logs(self, user, offset: int = None, limit: int = None, filters: str = None, sort_by: str = None):
        if not is_admin(user):
            return None, 403
        
        return self.next.audit_log_service_get_logs(user, offset, limit, filters, sort_by)

    def audit_log_service_get_logs_for_user(self, user, userid: int, offset: int = None, limit: int = None, filters: str = None, sort_by: str = None):
        if not is_admin_or_self(user, userid):
            return None, 403
        
        return self.next.audit_log_service_get_logs_for_user(user, userid, offset, limit, filters, sort_by)
