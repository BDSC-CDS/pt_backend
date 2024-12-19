import src.internal.api.server_template.controllers.dataset_controller as connexion_dataset_controller
import src.internal.api.controllers.dataset_controller as internal_dataset_controller
import src.internal.api.controllers.middleware.dataset_authorization as dataset_controller_authorization
import src.internal.api.controllers.middleware.dataset_audit as dataset_controller_audit
from src.internal.cmd.provider.audit_log import provide_audit_log_service
from src.pkg.dataset.service.dataset import DatasetService
from src.pkg.dataset.store.postgres import DatasetStore as PostgresDatasetStore
from .db import provide_db_type, provide_db
from .authentication import provide_authentication_service
from .clients import provide_jupyterhub_client
from .config import provide_config

dataset_controller = None
dataset_service = None
dataset_store = None

def provide_dataset_controller():
    global dataset_controller

    if dataset_controller is not None:
        return dataset_controller

    controller = internal_dataset_controller.DatasetController(provide_dataset_service())
    controller = dataset_controller_audit.DatasetControllerAudit(controller,provide_audit_log_service()) # TODO here ?
    controller = dataset_controller_authorization.DatasetControllerAuthentication(controller)
    dataset_controller = connexion_dataset_controller.DatasetController(controller)

    return dataset_controller

def provide_dataset_service():
    global dataset_service

    if dataset_service is not None:
        return dataset_service

    dataset_service = DatasetService(provide_config(), provide_dataset_store(), provide_authentication_service(), provide_jupyterhub_client())

    return dataset_service

def provide_dataset_store():
    global dataset_store

    if dataset_store is not None:
        return dataset_store

    tpe = provide_db_type()

    if tpe == "postgres":
        dataset_store = PostgresDatasetStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")


    return dataset_store
