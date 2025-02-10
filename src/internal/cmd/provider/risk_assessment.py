import src.internal.api.server_template.controllers.risk_assessment_service_controller as connexion_risk_assessment_controller
import src.internal.api.controllers.risk_assessment_controller as internal_risk_assessment_controller
import src.internal.api.controllers.middleware.risk_assessment_authorization as risk_assessment_controller_authorization
from src.pkg.risk_assessment.service.risk_assessment import RiskAssessmentService
from .config import provide_config
from .clients import provide_arx_client
from .dataset import provide_dataset_service
risk_assessment_controller = None
risk_assessment_service = None
risk_assessment_store = None

def provide_risk_assessment_controller():
    global risk_assessment_controller

    if risk_assessment_controller is not None:
        return risk_assessment_controller

    controller = internal_risk_assessment_controller.RiskAssessmentController(provide_config(), provide_risk_assessment_service())
    controller = risk_assessment_controller_authorization.RiskAssessmentControllerAuthentication(controller)
    risk_assessment_controller = connexion_risk_assessment_controller.RiskAssessmentController(controller)

    return risk_assessment_controller

def provide_risk_assessment_service():
    global risk_assessment_service

    if risk_assessment_service is not None:
        return risk_assessment_service

    # risk_assessment_service = RiskAssessmentService(provide_risk_assessment_store())
    risk_assessment_service = RiskAssessmentService(provide_arx_client(), provide_dataset_service())

    return risk_assessment_service

# def provide_risk_assessment_store():
#     global risk_assessment_store

#     if risk_assessment_store is not None:
#         return risk_assessment_store
    
#     tpe = provide_db_type()

#     if tpe == "postgres":
#         risk_assessment_store = PostgresRiskAssessmentStore(provide_db())
#         pass
#     else:
#         raise NotImplementedError("datastore type " + tpe + " is not implemented")
        

#     return risk_assessment_store