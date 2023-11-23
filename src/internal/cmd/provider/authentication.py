import src.internal.api.controllers.authentication_controller as internal_authentication_controller
import src.internal.api.server_template.controllers.authentication_controller as connexion_authentication_controller

authentication_controller = None

def provide_authentication_controller():
    global authentication_controller

    if authentication_controller is not None:
        return authentication_controller

    controller = internal_authentication_controller.AuthenticationController()
    print("contr", controller)
    authentication_controller = connexion_authentication_controller.AuthenticationController(controller)

    return authentication_controller