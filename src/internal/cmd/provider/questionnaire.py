import src.internal.api.server_template.controllers.questionnaire_service_controller as connexion_questionnaire_controller
import src.internal.api.controllers.questionnaire_controller as internal_questionnaire_controller
import src.internal.api.controllers.middleware.questionnaire_authorization as questionnaire_controller_authorization
from src.pkg.questionnaire.service.questionnaire import QuestionnaireService
from src.pkg.questionnaire.store.postgres import QuestionnaireStore as PostgresQuestionnaireStore
from .config import provide_config
from .db import provide_db_type, provide_db

questionnaire_controller = None
questionnaire_service = None
questionnaire_store = None

def provide_questionnaire_controller():
    global questionnaire_controller

    if questionnaire_controller is not None:
        return questionnaire_controller

    controller = internal_questionnaire_controller.QuestionnaireServiceController(provide_config(), provide_questionnaire_service())
    controller = questionnaire_controller_authorization.QuestionnaireServiceControllerAuthentication(controller)
    questionnaire_controller = connexion_questionnaire_controller.QuestionnaireServiceController(controller)

    return questionnaire_controller

def provide_questionnaire_service():
    global questionnaire_service

    if questionnaire_service is not None:
        return questionnaire_service

    questionnaire_service = QuestionnaireService(provide_questionnaire_store())

    return questionnaire_service

def provide_questionnaire_store():
    global questionnaire_store

    if questionnaire_store is not None:
        return questionnaire_store
    
    tpe = provide_db_type()

    if tpe == "postgres":
        questionnaire_store = PostgresQuestionnaireStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")
        

    return questionnaire_store