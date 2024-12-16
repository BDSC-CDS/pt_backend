from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment
import pandas as pd


class RiskAssessmentService:
    def __init__(self, arx_client, dataset_service):
        self.arx_client = arx_client
        self.dataset_service = dataset_service

    def get_risk_assessment(self, tenantid: int, userid: int, dataset_id: int) -> RiskAssessment:
        columns_as_lists, total_rows = self.dataset_service.get_dataset_content(dataset_id, userid, tenantid)
        dataset = pd.DataFrame(columns_as_lists).transpose()
        dataset.columns = [f"Column_{i}" for i in range(dataset.shape[1])]

        json_config = None 

        initial_highest_prosecutor, initial_average_prosecutor, quasi_identifiers, risk_assessment_server_answer = self.arx_client.perform_risk_analysis(dataset, json_config)
        return RiskAssessment(
            userid=self.userid,
            tenantid=self.tenantid,
            dataset_id=self.dataset_id,
            average_prosecutor_risk = initial_average_prosecutor,
            maximum_prosecutor_risk = initial_highest_prosecutor,
            quasi_identifiers = quasi_identifiers,   
            risk_assessment=risk_assessment_server_answer
        )
