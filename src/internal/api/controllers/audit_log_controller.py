import src.internal.api.controllers.converter.audit_log as audit_log_converter

class AuditLogController:
    def __init__(self, config, auditlog_service):
        self.config = config
        self.auditlog_service = auditlog_service

    def audit_log_service_get_logs(self, user, offset: int=None, limit: int=None):
        logs = self.audit_log_service.get_logs(offset, limit)
        logs = audit_log_converter.audit_log_from_business(logs)
        return logs


    def audit_log_service_get_logs_for_user(self, user, userid: int, offset: int=None, limit: int=None):
        logs = self.audit_log_service.get_logs_for_user(userid, offset, limit)
        logs = audit_log_converter.audit_log_from_business(logs)
        return logs

