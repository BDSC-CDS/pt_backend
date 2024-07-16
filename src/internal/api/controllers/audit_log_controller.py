from server_template.models.templatebackend_get_logs_response import TemplatebackendGetLogsResponse
import src.internal.api.controllers.converter.audit_log as audit_log_converter

class AuditLogController:
    def __init__(self, config, audit_log_service):
        self.config = config
        self.audit_log_service = audit_log_service

    def audit_log_service_get_logs(self, user, offset: int = None, limit: int = None, filters: dict = None, sort_by: str = None) -> TemplatebackendGetLogsResponse:
        print("get logs", user, offset, limit, filters, sort_by)
        logs = self.audit_log_service.get_logs(offset, limit, filters, sort_by)
        logs = audit_log_converter.audit_logs_from_business(logs)
        return TemplatebackendGetLogsResponse(logs)

    def audit_log_service_get_logs_for_user(self, user, userid: int, offset: int = None, limit: int = None, filters: dict = None, sort_by: str = None):
        logs = self.audit_log_service.get_logs_for_user(userid, offset, limit, filters, sort_by)
        logs = audit_log_converter.audit_logs_from_business(logs)
        return TemplatebackendGetLogsResponse(logs)
