import src.internal.api.server_template.controllers.configuration_controller as connexion_config_generator_controller
import src.internal.api.controllers.config_gen_controller as internal_config_generator_controller
# import src.internal.api.controllers.middleware.dataset_authorization as dataset_controller_authorization
# import src.internal.api.controllers.middleware.dataset_audit as dataset_controller_audit
# from src.internal.cmd.provider.config_generator import provide_audit_log_service
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

    controller = internal_config_generator_controller.ConfigGeneratorController(provide_config_generator_service())
    # controller = dataset_controller_audit.DatasetControllerAudit(controller,provide_audit_log_service()) # TODO here ?
    # controller = dataset_controller_authorization.DatasetControllerAuthentication(controller)
    config_generator_controller = connexion_config_generator_controller.ConfigurationController(controller)

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
