from src.internal.api.controllers import security_controller
import src.internal.api.controllers.audit_log_controller as internal_audit_log_controller
import src.internal.api.server_template.controllers.audit_log_controller as connexion_audit_log_controller
import src.internal.api.controllers.middleware.audit_log_authorization as audit_log_controller_authorization
from src.pkg.audit_log.service.audit_log import AuditLogService
from .config import provide_config

audit_log_controller = None
audit_log_service = None

def provide_audit_log_controller():
    global audit_log_controller

    if audit_log_controller is not None:
        return audit_log_controller

    controller = internal_audit_log_controller.AuditLogController(provide_config(), provide_audit_log_service())
    controller = audit_log_controller_authorization.AuditLogControllerAuthentication(controller)
    audit_log_controller = connexion_audit_log_controller.AuditLogController(controller)

    security_controller.inject_dependencies(provide_config(), provide_audit_log_service())

    return audit_log_controller

def provide_audit_log_service():
    global audit_log_service

    if audit_log_service is not None:
        return audit_log_service

    audit_log_service = AuditLogService(provide_config())

    return audit_log_service
