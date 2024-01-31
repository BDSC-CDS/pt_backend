from server_template.models import TemplatebackendCredentials
from server_template.models import TemplatebackendAuthenticationReply
from server_template.models import TemplatebackendAuthenticationResult

class AuthenticationController():
    def __init__(self, config, authentication_service):
        self.config = config
        self.authentication_service = authentication_service

    def authentication_service_authenticate(self, user, body: TemplatebackendCredentials):
        token = self.authentication_service.authenticate(body.username, body.password)
        return TemplatebackendAuthenticationReply(TemplatebackendAuthenticationResult(token)), 200
