import pandas as pd
from python_arx_deidentifier.client.assessment_client import apply_assessment
from python_arx_deidentifier.client.configuration_client import (
    build_basic_configuration,
    set_data_as_csv,
    set_nb_solutions,
    set_suppression_limit,
    set_is_used_population_model,
    configure_attribute,
)
from src.pkg.dataset.store.postgres import get_dataset_content
from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment


class RiskAssessmentService:
    """
    Service to manage risk assessment using ARX de-identification client.
    
    This class handles the configuration of ARX risk assessment based on user-provided
    settings and performs risk analysis on a specified dataset.
    """

    # TODO what do I do with the arx_client here? it's supposed to be the domain
    # TODO 
    def __init__(self, arx_client: str, dataset_id: int, tenantid: int, userid: int, risk_assessment_store):
        """
        Initializes the RiskAssessmentService.

        Args:
            arx_client: The ARX de-identification client instance.
            dataset_id (int): ID of the dataset to be analyzed.
            tenantid (int): ID of the tenant for multitenancy support.
            userid (int): ID of the user initiating the analysis.
        """
        self.arx_client = arx_client
        self.dataset_id = dataset_id
        self.tenantid = tenantid
        self.userid = userid
        self.risk_assessment_store = risk_assessment_store
        
# TODO add store and list


    @staticmethod
    def populate_config_from_dict(json_config: dict):
        """
        Builds and populates the ARX configuration object from a JSON-like dictionary.

        Args:
            json_config (dict): Configuration data including general settings and attribute details.
                Expected format:
                {
                    "nb_solutions": int,
                    "suppression_limit": float,
                    "is_used_population_model": bool,
                    "attributes": [
                        {
                            "key": str,
                            "source": str or None,
                            "type": str,
                            "weight": float or None
                        },
                        ...
                    ]
                }

        Returns:
            arx_config: Configured ARX configuration object.
        """
        arx_config = build_basic_configuration()

        # Set general configurations
        arx_config = set_nb_solutions(arx_config, json_config["nb_solutions"])
        arx_config = set_suppression_limit(arx_config, json_config["suppression_limit"])
        arx_config = set_is_used_population_model(arx_config, json_config["is_used_population_model"])

        # Configure individual attributes
        for attr in json_config["attributes"]:
            arx_config = configure_attribute(
                arx_config,
                attr["key"],
                attr.get("source"),
                attr["type"],
                attr.get("weight"),
            )

        return arx_config

    def get_risk_assessment(self, json_config: dict) -> RiskAssessment:
        """
        Retrieves the risk assessment results for the dataset using provided configurations.

        Args:
            json_config (dict): Configuration data for risk assessment.

        Returns:
            RiskAssessment: A RiskAssessment object containing the results of the analysis.
        """
        # Fetch dataset content
        dataset = get_dataset_content(self.dataset_id, self.userid, self.tenantid)

        # Perform risk analysis
        risk_assessment_result = self.perform_risk_analysis(dataset, json_config)

        return risk_assessment_result

    def perform_risk_analysis(self, dataset: pd.DataFrame, json_config: dict) -> RiskAssessment:
        """
        Executes the risk analysis process for a given dataset and configuration.

        Args:
            dataset (pd.DataFrame): The dataset to be analyzed.
            json_config (dict): Configuration data for risk assessment.

        Returns:
            RiskAssessment: A RiskAssessment object encapsulating the results.
        """
        # Build the ARX configuration
        arx_config = self.populate_config_from_dict(json_config)

        # Link dataset to the configuration
        arx_config = set_data_as_csv(arx_config, dataset)

        # Apply the risk assessment
        risk_assessment_result = apply_assessment(self.arx_client, arx_config)

        return RiskAssessment(
            userid=self.userid,
            dataset_id=self.dataset_id,
            tenantid=self.tenantid,
            risk_assessment=risk_assessment_result
        )
