import src.internal.api.server_template.controllers.configuration_controller as connexion_config_controller
import src.internal.api.controllers.config_gen_controller as internal_config_controller
import src.internal.api.controllers.middleware.config_gen_authorization as config_controller_authorization
import src.internal.api.controllers.middleware.config_gen_audit as config_controller_audit
from src.internal.cmd.provider.audit_log import provide_audit_log_service
from src.pkg.config_generator.service.config_generator import ConfigGeneratorService
from src.pkg.config_generator.store.postgres import ConfigGeneratorStore as PostgresConfigStore
from .db import provide_db_type, provide_db

config_gen_controller = None
config_gen_service = None
config_gen_store = None

def provide_config_gen_controller():
    global config_gen_controller

    if config_gen_controller is not None:
        return config_gen_controller

    controller = internal_config_controller.ConfigGeneratorController(provide_config_gen_service())
    controller = config_controller_audit.ConfigGeneratorControllerAudit(controller,provide_audit_log_service())
    controller = config_controller_authorization.ConfigGeneratorControllerAuthentication(controller)
    config_gen_controller = connexion_config_controller.ConfigurationController(controller)

    return config_gen_controller

def provide_config_gen_service():
    global config_gen_service

    if config_gen_service is not None:
        return config_gen_service

    config_gen_service = ConfigGeneratorService(provide_config_gen_store())

    return config_gen_service

def provide_config_gen_store():
    global config_gen_store

    if config_gen_store is not None:
        return config_gen_store

    tpe = provide_db_type()

    if tpe == "postgres":
        config_gen_store = PostgresConfigStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")


    return config_gen_store
