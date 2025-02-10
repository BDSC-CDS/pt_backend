import src.internal.api.server_template.controllers.users_service_controller as connexion_user_controller
import src.internal.api.controllers.user_controller as internal_user_controller
import src.internal.api.controllers.middleware.user_authorization as user_controller_authorization
import src.internal.api.controllers.middleware.user_audit as user_controller_audit
from src.internal.cmd.provider.audit_log import provide_audit_log_service
from src.pkg.user.service.user import UserService
from src.pkg.user.store.postgres import UserStore as PostgresUserStore
from .db import provide_db_type, provide_db

user_controller = None
users_service = None
user_store = None

def provide_user_controller():
    global user_controller

    if user_controller is not None:
        return user_controller

    controller = internal_user_controller.UsersServiceController(provide_users_service())
    controller = user_controller_audit.UsersServiceControllerAudit(controller,provide_audit_log_service()) # TODO here ?
    controller = user_controller_authorization.UsersServiceControllerAuthentication(controller)
    user_controller = connexion_user_controller.UsersServiceController(controller)

    return user_controller

def provide_users_service():
    global users_service

    if users_service is not None:
        return users_service

    users_service = UserService(provide_user_store())

    return users_service

def provide_user_store():
    global user_store

    if user_store is not None:
        return user_store

    tpe = provide_db_type()

    if tpe == "postgres":
        user_store = PostgresUserStore(provide_db())
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")


    return user_store
