from src.internal.api.controllers.risk_assessment_controller import RiskAssessmentController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class RiskAssessmentControllerAuthentication():
    def __init__(self, next: RiskAssessmentController):
        self.next = next
        implements_interface(RiskAssessmentControllerAuthentication, RiskAssessmentController)

    def risk_assessment_service_get_risk_assessment(self, user):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.risk_assessment_service_get_risk_assessment(user)
