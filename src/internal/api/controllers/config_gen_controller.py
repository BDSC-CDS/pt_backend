from server_template.models import TemplatebackendCredentials
from server_template.models import TemplatebackendAuthenticationReply
from server_template.models import TemplatebackendAuthenticationResult
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.config_generator.model.config_generator import ConfigGenerator

class ConfigGeneratorController():
    def __init__(self, config, configgenerator_service,auditlog_service):
        self.configgenerator_service = configgenerator_service
        self.auditlog_service = auditlog_service

    # def authentication_service_authenticate(self, user, body: ConfigGenerator):
    #     try:
    #         token = self.authentication_service.authenticate(body.username, body.password)
    #         self.auditlog_service.log_event(AuditLog(service="ConfigGeneratorController", action="created config file",body=body.username))
    #         return TemplatebackendAuthenticationReply(TemplatebackendAuthenticationResult(token)), 200
    #     except Exception as e:
    #         self.auditlog_service.log_event(AuditLog(service="AuthenticationController", action="Error authenticating",body=body.username, error=True))
    #         raise e
