import src.internal.api.server_template.controllers.dataset_controller as connexion_dataset_controller
import src.internal.api.controllers.dataset_controller as internal_dataset_controller
from .config import provide_config
from .db import provide_db_type, provide_db

# TODO REDO THIS FILE
dataset_controller = None
dataset_service = None
dataset_store = None

def provide_dataset_controller():
    global dataset_controller

    if dataset_controller is not None:
        return dataset_controller

    controller = internal_dataset_controller.DatasetController(provide_config(), provide_dataset_service())
    dataset_controller = connexion_dataset_controller.DatasetController(controller)

    return dataset_controller

def provide_dataset_service():
    global dataset_service

    if dataset_service is not None:
        return dataset_service

    # dataset_service = DatasetService(provide_dataset_store())

    return dataset_service

def provide_dataset_store():
    global dataset_store

    if dataset_store is not None:
        return dataset_store

    tpe = provide_db_type()

    if tpe == "postgres":
        # dataset_store = PostgresDatasetStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")


    return dataset_store
