from src.internal.api.controllers.security_controller import inject_dependencies
import src.internal.api.controllers.authentication_controller as internal_authentication_controller
import src.internal.api.server_template.controllers.authentication_controller as connexion_authentication_controller
from src.pkg.authentication.service.authentication import AuthenticationService
from .user import provide_user_service
from .config import provide_config

authentication_controller = None
authentication_service = None

def provide_authentication_controller():
    global authentication_controller

    if authentication_controller is not None:
        return authentication_controller

    controller = internal_authentication_controller.AuthenticationController(provide_config(), provide_authentication_service())
    authentication_controller = connexion_authentication_controller.AuthenticationController(controller)

    inject_dependencies(provide_config(), provide_user_service())

    return authentication_controller

def provide_authentication_service():
    global authentication_service

    if authentication_service is not None:
        return authentication_service

    authentication_service = AuthenticationService(provide_config(), provide_user_service())

    return authentication_service