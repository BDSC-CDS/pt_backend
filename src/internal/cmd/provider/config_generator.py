import src.internal.api.server_template.controllers.configuration_service_controller as connexion_config_controller
import src.internal.api.controllers.config_generator_controller as internal_config_controller
import src.internal.api.controllers.middleware.config_generator_authorization as config_controller_authorization
import src.internal.api.controllers.middleware.config_generator_audit as config_controller_audit
from src.internal.cmd.provider.audit_log import provide_audit_log_service
from src.pkg.config_generator.service.config_generator import ConfigGeneratorService
from src.pkg.config_generator.store.postgres import ConfigGeneratorStore as PostgresConfigStore
from .db import provide_db_type, provide_db

config_generator_controller = None
config_generator_service = None
config_generator_store = None

def provide_config_generator_controller():
    global config_generator_controller

    if config_generator_controller is not None:
        return config_generator_controller

    controller = internal_config_controller.ConfigGeneratorController(provide_config_generator_service())
    controller = config_controller_audit.ConfigGeneratorControllerAudit(controller,provide_audit_log_service())
    controller = config_controller_authorization.ConfigGeneratorControllerAuthentication(controller)
    config_generator_controller = connexion_config_controller.ConfigurationController(controller)

    return config_generator_controller

def provide_config_generator_service():
    global config_generator_service

    if config_generator_service is not None:
        return config_generator_service

    config_generator_service = ConfigGeneratorService(provide_config_generator_store())

    return config_generator_service

def provide_config_generator_store():
    global config_generator_store

    if config_generator_store is not None:
        return config_generator_store

    tpe = provide_db_type()

    if tpe == "postgres":
        config_generator_store = PostgresConfigStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")


    return config_generator_store
