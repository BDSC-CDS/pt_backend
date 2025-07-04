from src.internal.api.controllers.risk_assessment_controller import RiskAssessmentServiceController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class RiskAssessmentServiceControllerAuthentication():
    def __init__(self, next: RiskAssessmentServiceController):
        self.next = next
        implements_interface(RiskAssessmentServiceControllerAuthentication, RiskAssessmentServiceController)

    def risk_assessment_service_get_risk_assessment(self, user, datasetid: int):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.risk_assessment_service_get_risk_assessment(user, datasetid)
