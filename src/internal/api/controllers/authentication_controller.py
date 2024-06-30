from server_template.models import TemplatebackendCredentials
from server_template.models import TemplatebackendAuthenticationReply
from server_template.models import TemplatebackendAuthenticationResult
from src.pkg.audit_log.model.audit_log import AuditLog

class AuthenticationController():
    def __init__(self, config, authentication_service,audit_log_service):
        self.config = config
        self.authentication_service = authentication_service
        self.audit_log_service = audit_log_service

    def authentication_service_authenticate(self, user, body: TemplatebackendCredentials):
        try:
            token = self.authentication_service.authenticate(body.username, body.password)
            self.audit_log_service.log_event(AuditLog(service="AuthenticationController", action="authenticated user",body=body.username))
            return TemplatebackendAuthenticationReply(TemplatebackendAuthenticationResult(token)), 200
        except Exception as e:
            self.audit_log_service.log_event(AuditLog(service="AuthenticationController", action="Error authenticating",body=body.username, error=True))
            raise e
