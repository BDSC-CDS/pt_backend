from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment


class RiskAssessmentService:
    def __init__(self, arx_client):
        self.arx_client = arx_client

    def get_risk_assessment(self, tenantid: int, userid: int) -> RiskAssessment:
        records = self.arx_client.get_all_records()
        return records
    