from server_template.models.templatebackend_get_logs_response import TemplatebackendGetLogsResponse
import src.internal.api.controllers.converter.audit_log as audit_log_converter
import json

class AuditLogServiceController:
    def __init__(self, config, audit_log_service):
        self.config = config
        self.audit_log_service = audit_log_service

    def audit_log_service_get_logs(self, user, offset: int = None, limit: int = None, filters: str = None, sort_by: str = None) -> TemplatebackendGetLogsResponse:
        # Convert filters to a dictionary for internal processing if needed
        filters_dict = json.loads(filters) if filters else {}
        
        if limit is None:
            limit = 100

        if offset is None:
            offset = 0
        
        logs = self.audit_log_service.get_logs(offset, limit, filters_dict, sort_by)
        logs = audit_log_converter.audit_logs_from_business(logs)
        return TemplatebackendGetLogsResponse(logs)

    def audit_log_service_get_logs_for_user(self, user, userid: int, offset: int = None, limit: int = None, filters: str = None, sort_by: str = None):
        filters_dict = json.loads(filters) if filters else {}
        logs = self.audit_log_service.get_logs_for_user(userid, offset, limit, filters, sort_by)
        logs = audit_log_converter.audit_logs_from_business(logs)
        return TemplatebackendGetLogsResponse(logs)
