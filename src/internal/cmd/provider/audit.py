import src.internal.api.controllers.audit_controller as internal_audit_controller
from src.internal.api.services.audit_service import AuditService
from src.internal.api.stores.audit_store import AuditStore
from .config import provide_config
from .db import provide_db_type, provide_db

audit_controller = None
audit_service = None
audit_store = None

def provide_audit_controller():
    global audit_controller

    if audit_controller is not None:
        return audit_controller

    controller = internal_audit_controller.AuditController(provide_config(), provide_audit_service())
    audit_controller = controller

    return audit_controller

def provide_audit_service():
    global audit_service

    if audit_service is not None:
        return audit_service

    audit_service = AuditService(provide_audit_store())

    return audit_service

def provide_audit_store():
    global audit_store

    if audit_store is not None:
        return audit_store

    tpe = provide_db_type()

    if tpe == "postgres":
        audit_store = AuditStore(provide_db())
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")

    return audit_store
