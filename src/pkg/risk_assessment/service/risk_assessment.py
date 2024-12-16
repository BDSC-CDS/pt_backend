from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment
import pandas as pd


class RiskAssessmentService:
    def __init__(self, arx_client, dataset_service):
        self.arx_client = arx_client
        self.dataset_service = dataset_service

    def get_risk_assessment(self,  dataset_id: int, tenantid: int, userid: int, json_config: dict) -> RiskAssessment:
        columns_as_lists, total_rows = self.dataset_service.get_dataset_content(dataset_id, userid, tenantid)
        dataset = pd.DataFrame(columns_as_lists).transpose()
        dataset.columns = [f"Column_{i}" for i in range(df.shape[1])]
        initial_highest_prosecutor, initial_average_prosecutor, quasi_identifiers, risk_assessment_server_answer = self.arx_client.perform_risk_analysis(dataset, json_config)
        return RiskAssessment(
            userid=self.userid,
            dataset_id=self.dataset_id,
            tenantid=self.tenantid,
            average_prosecutor_risk = initial_average_prosecutor,
            maximum_prosecutor_risk = initial_highest_prosecutor,
            quasi_identifiers = quasi_identifiers,   
            risk_assessment=risk_assessment_server_answer
        )
