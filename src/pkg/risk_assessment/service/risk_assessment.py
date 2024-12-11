from src.pkg.dataset.store.postgres import get_dataset_content
from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment
from src.clients.arx.client import provide_arx_client, perform_risk_analysis

class RiskAssessmentService:
    def __init__(self, dataset_id: int, tenantid: int, userid: int, risk_assessment_store):
        self.dataset_id = dataset_id
        self.tenantid = tenantid
        self.userid = userid
        self.risk_assessment_store = risk_assessment_store
        self.arx_client = provide_arx_client()

    def get_risk_assessment(self, json_config: dict) -> RiskAssessment:
        dataset = get_dataset_content(self.dataset_id, self.userid, self.tenantid)
        initial_highest_prosecutor, initial_average_prosecutor, quasi_identifiers, risk_assessment_server_answer = perform_risk_analysis(dataset, json_config, self.arx_client)
        return RiskAssessment(
            userid=self.userid,
            dataset_id=self.dataset_id,
            tenantid=self.tenantid,
            average_prosecutor_risk = initial_average_prosecutor,
            maximum_prosecutor_risk = initial_highest_prosecutor,
            quasi_identifiers = quasi_identifiers,   
            risk_assessment=risk_assessment_server_answer
        )
