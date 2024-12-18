from server_template.models import TemplatebackendGetRiskAssessmentResult
from server_template.models import TemplatebackendGetRiskAssessmentReply


# import src.internal.api.controllers.converter.risk_assessment as risk_assessment_converter


class RiskAssessmentController:
    def __init__(self, config, risk_assessment_service):
        self.config = config
        self.risk_assessment_service = risk_assessment_service

    def risk_assessment_service_get_risk_assessment(self, user, dataset_id: int = None):
        records = self.risk_assessment_service.get_risk_assessment(user.tenantid, user.id, dataset_id)

        
        return TemplatebackendGetRiskAssessmentReply(TemplatebackendGetRiskAssessmentResult(records))

