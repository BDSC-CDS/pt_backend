import src.internal.api.server_template.controllers.transform_config_service_controller as connexion_transform_config_controller
import src.internal.api.controllers.transform_config_controller as internal_config_controller
import src.internal.api.controllers.middleware.transform_config_authorization as config_controller_authorization
import src.internal.api.controllers.middleware.transform_config_audit as config_controller_audit
from src.internal.cmd.provider.audit_log import provide_audit_log_service
from src.pkg.transform_config.service.transform_config import TransformConfigService
from src.pkg.transform_config.store.postgres import TransformConfigStore as PostgresConfigStore
from .db import provide_db_type, provide_db

transform_config_controller = None
transform_config_service = None
transform_config_store = None

def provide_transform_config_controller():
    global transform_config_controller

    if transform_config_controller is not None:
        return transform_config_controller

    controller = internal_config_controller.TransformConfigServiceController(provide_transform_config_service())
    controller = config_controller_audit.TransformConfigServiceControllerAudit(controller,provide_audit_log_service())
    controller = config_controller_authorization.TransformConfigServiceControllerAuthentication(controller)
    transform_config_controller = connexion_transform_config_controller.TransformConfigServiceController(controller)

    return transform_config_controller

def provide_transform_config_service():
    global transform_config_service

    if transform_config_service is not None:
        return transform_config_service

    transform_config_service = TransformConfigService(provide_transform_config_store())

    return transform_config_service

def provide_transform_config_store():
    global transform_config_store

    if transform_config_store is not None:
        return transform_config_store

    tpe = provide_db_type()

    if tpe == "postgres":
        transform_config_store = PostgresConfigStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")

    return transform_config_store
