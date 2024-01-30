from server_template.models.templatebackend_credentials import TemplatebackendCredentials
from server_template.models.templatebackend_authentication_reply import TemplatebackendAuthenticationReply
from server_template.models.templatebackend_authentication_result import TemplatebackendAuthenticationResult
from server_template import util

class AuthenticationController():
    def __init__(self, config, authentication_service):
        self.config = config
        self.authentication_service = authentication_service

    def authentication_service_authenticate(self, user, body: TemplatebackendCredentials):
        token = self.authentication_service.authenticate(body.username, body.password)
        return TemplatebackendAuthenticationReply(TemplatebackendAuthenticationResult(token)), 200
