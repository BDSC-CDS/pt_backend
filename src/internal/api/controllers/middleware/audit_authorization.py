from src.internal.api.models import TemplatebackendAddLogRequest
from src.internal.api.controllers.audit_controller import AuditController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class AuditControllerAuthentication:
    def __init__(self, next: AuditController):
        self.next = next
        implements_interface(AuditController, AuditControllerAuthentication)

    def add_log(self, user, body: TemplatebackendAddLogRequest):
        if not is_authenticated(user):
            return None, 403

        return self.next.add_log(user, body)
