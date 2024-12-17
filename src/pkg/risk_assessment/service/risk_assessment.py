from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment
import pandas as pd


class RiskAssessmentService:
    def __init__(self, arx_client, dataset_service):
        self.arx_client = arx_client
        self.dataset_service = dataset_service

    def create_arx_config_from_metadata(
        self, tenantid: int, userid: int, dataset_id: int
    ):
        """
        Transforms input JSON metadata to fit the configuration function format.
        Maps identifier types to ARX-compatible attribute types.

        Args:
            input_json (dict): Input JSON metadata with columns and attributes.

        Returns:
            dict: Transformed configuration as a dictionary.
        """
        metadata = self.dataset_service.get_dataset_metadata(
            dataset_id, userid, tenantid
        )

        # Define the mapping for identifier types
        identifier_mapping = {
            "identifier": "IDENTIFYING_ATTRIBUTE",
            "quasi-identifier": "QUASI_IDENTIFYING_ATTRIBUTE",
            "non-identifying": "INSENSITIVE_ATTRIBUTE",
        }

        transformed_config = {"attributes": []}

        # Extract the list of metadata items
        metadata_items = metadata.get("metadata", {}).get("metadata", [])

        # Transform each metadata entry into the required format
        for item in metadata_items:
            transformed_config["attributes"].append(
                {
                    "key": item["columnName"],  # The column name becomes the key
                    "type": identifier_mapping.get(
                        item["identifier"], "INSENSITIVE_ATTRIBUTE"
                    ),  # Map identifier type
                    "weight": None,  # Weight is always set to None
                }
            )

        return transformed_config

    def get_risk_assessment(
        self, tenantid: int, userid: int, dataset_id: int
    ) -> RiskAssessment:
        columns_as_lists, total_rows = self.dataset_service.get_dataset_content(
            dataset_id, userid, tenantid
        )

        # transform dataset into dataframe
        dataset = pd.DataFrame(columns_as_lists).transpose()
        dataset.columns = [f"Column_{i}" for i in range(dataset.shape[1])]

        json_config = self.create_arx_config_from_metadata(tenantid, userid, dataset_id)

        (
            initial_highest_prosecutor,
            initial_average_prosecutor,
            quasi_identifiers,
            risk_assessment_server_answer,
        ) = self.arx_client.perform_risk_analysis(dataset, json_config)
        return RiskAssessment(
            userid=self.userid,
            tenantid=self.tenantid,
            dataset_id=self.dataset_id,
            average_prosecutor_risk=initial_average_prosecutor,
            maximum_prosecutor_risk=initial_highest_prosecutor,
            quasi_identifiers=quasi_identifiers,
            risk_assessment=risk_assessment_server_answer,
        )
