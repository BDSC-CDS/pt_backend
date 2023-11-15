from . import config
import src.internal.api.server_template.controllers.authentication_controller as connexion_authentication_controller
import src.internal.api.server_template.controllers.index_controller as connexion_index_controller
import src.internal.api.server_template.controllers.users_controller as connexion_users_controller

import src.internal.api.controllers.authentication_controller as internal_authentication_controller
import src.internal.api.controllers.index_controller as internal_index_controller
import src.internal.api.controllers.users_controller as internal_users_controller

controllers = None
authentication_controller = None
index_controller = None
users_controller = None

def provide_controllers():
    global controllers

    if controllers is not None:
        return controllers

    controllers = {}
    
    controllers['authentication_controller'] = provide_authentication_controller()
    controllers['index_controller'] = provide_index_controller()
    controllers['users_controller'] = provide_users_controller()

    return controllers

    
def provide_authentication_controller():
    global authentication_controller

    if authentication_controller is not None:
        return authentication_controller

    controller = internal_authentication_controller.AuthenticationController()
    print("contr", controller)
    authentication_controller = connexion_authentication_controller.AuthenticationController(controller)

    return authentication_controller

def provide_index_controller():
    global index_controller

    if index_controller is not None:
        return index_controller
    
    controller = internal_index_controller.IndexController()
    index_controller = connexion_index_controller.IndexController(controller)

    return index_controller

def provide_users_controller():
    global users_controller

    if users_controller is not None:
        return users_controller

    controller = internal_users_controller.UsersController()
    users_controller = connexion_users_controller.UsersController(controller)

    return users_controller
     


