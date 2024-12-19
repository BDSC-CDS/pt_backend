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
        Transforms input metadata to fit the configuration function format.
        Maps identifier types to ARX-compatible attribute types.

        Args:
            tenantid (int): Tenant ID.
            userid (int): User ID.
            dataset_id (int): Dataset ID.

        Returns:
            dict: Transformed configuration as a dictionary.
        """
        # Fetch the metadata
        metadata_items = self.dataset_service.get_dataset_metadata(
            dataset_id, userid, tenantid
        )

        if metadata_items is None:
            raise ValueError("No metadata found for the specified dataset.")

        # Define the mapping for identifier types
        identifier_mapping = {
            "identifier": "IDENTIFYING_ATTRIBUTE",
            "quasi-identifier": "QUASI_IDENTIFYING_ATTRIBUTE",
            "non-identifying": "INSENSITIVE_ATTRIBUTE",
        }

        transformed_config = {"attributes": []}

        # Transform each metadata entry into the required format
        for item in metadata_items:
            transformed_config["attributes"].append(
                {
                    "key": item.column_name,  # Use the column_name attribute
                    "type": identifier_mapping.get(
                        item.identifier, "INSENSITIVE_ATTRIBUTE"
                    ),  # Map identifier type
                    "weight": None,  # Weight is always set to None
                }
            )

        return transformed_config

    def get_risk_assessment(
        self, tenantid: int, userid: int, dataset_id: int
    ) -> RiskAssessment:
        columns_as_lists, _ = self.dataset_service.get_dataset_content(
            dataset_id, userid, tenantid, offset=0, limit=1000,
        )
        metadata = self.dataset_service.get_dataset_metadata(
            dataset_id, userid, tenantid, 
        )

        column_names = []
        for item in metadata:
            flattened_name = ''.join([str(level) for level in item.column_name])
            column_names.append(flattened_name)

        # transform dataset into dataframe
        dataset = pd.DataFrame(columns_as_lists).transpose()
        dataset.columns = column_names


        json_config = self.create_arx_config_from_metadata(tenantid, userid, dataset_id)

        (
            initial_highest_prosecutor,
            initial_average_prosecutor,
            quasi_identifiers,
            risk_assessment_server_answer,
        ) = self.arx_client.perform_risk_analysis(dataset, json_config)

        return RiskAssessment(
            userid=userid,
            tenantid=tenantid,
            dataset_id=dataset_id,
            average_prosecutor_risk=initial_average_prosecutor,
            maximum_prosecutor_risk=initial_highest_prosecutor,
            quasi_identifiers=quasi_identifiers,
            risk_assessment=risk_assessment_server_answer,
        )
