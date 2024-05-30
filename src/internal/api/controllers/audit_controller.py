from src.internal.api.models import TemplatebackendAddLogRequest, TemplatebackendAddLogResponse
from src.internal.api.services.audit_service import AuditService
from src.internal.api.auth import is_admin

class AuditController:
    def __init__(self, config, audit_service: AuditService):
        self.config = config
        self.audit_service = audit_service

    def add_log(self, user, body: TemplatebackendAddLogRequest) -> TemplatebackendAddLogResponse:
        if not is_admin(user):
            raise PermissionError("Unauthorized")
        
        response = self.audit_service.add_log(body)
        return response
