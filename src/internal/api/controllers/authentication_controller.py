import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from inspect import getmembers, isfunction


from server_template.models.rpc_status import RpcStatus
from server_template.models.templatebackend_credentials import TemplatebackendCredentials
from server_template.models.templatebackend_authentication_reply import TemplatebackendAuthenticationReply
from server_template.models.templatebackend_authentication_result import TemplatebackendAuthenticationResult
from server_template import util

class AuthenticationController():
    def authentication_service_authenticate(self, body: TemplatebackendCredentials):
        return TemplatebackendAuthenticationReply(TemplatebackendAuthenticationResult("hello")), 200
