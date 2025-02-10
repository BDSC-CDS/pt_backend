from src.internal.api.controllers.audit_log_controller import AuditLogServiceController
from src.internal.api.controllers.middleware.audit_log_authorization import AuditLogServiceControllerAuthentication
from src.pkg.audit_log.service.audit_log import AuditLogService
from .config import provide_config
from src.pkg.audit_log.store.postgres import AuditLogStore as PostgresAuditStore
from .db import provide_db_type, provide_db

audit_log_controller = None
audit_log_service = None
audit_log_store = None

def provide_audit_log_controller():
    global audit_log_controller

    if audit_log_controller is not None:
        return audit_log_controller

    controller = AuditLogServiceController(provide_config(), provide_audit_log_service())
    controller = AuditLogServiceControllerAuthentication(controller)
    audit_log_controller = controller

    return audit_log_controller

def provide_audit_log_service():
    global audit_log_service

    if audit_log_service is not None:
        return audit_log_service

    audit_log_service = AuditLogService(provide_audit_log_store())

    return audit_log_service

def provide_audit_log_store():
    global audit_log_store

    if audit_log_store is not None:
        return audit_log_store

    tpe = provide_db_type()

    if tpe == "postgres":
        audit_log_store = PostgresAuditStore(provide_db())
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")

    return audit_log_store
