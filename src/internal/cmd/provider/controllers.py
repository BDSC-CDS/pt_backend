from . import config
from .authentication import provide_authentication_controller
from .index import provide_index_controller
from .user import provide_user_controller
from .dataset import provide_dataset_controller
controllers = None

def provide_controllers():
    global controllers

    if controllers is not None:
        return controllers

    controllers = {}

    controllers['authentication_controller'] = provide_authentication_controller()
    controllers['index_controller'] = provide_index_controller()
    controllers['user_controller'] = provide_user_controller()
    controllers['dataset_controller'] = provide_dataset_controller()

    return controllers
