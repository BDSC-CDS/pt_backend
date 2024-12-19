from python_arx_deidentifier.client.assessment_client import (
    apply_assessment,
    parse_risk_assessment,
)
from python_arx_deidentifier.client.configuration_client import (
    build_basic_configuration,
    set_data_as_csv,
    configure_attribute,
)
import pandas as pd


class ArxClient:
    def __init__(self, config):
        self.host = config.host

    def build_config_from_dict(self, json_config: dict, dataset):
        """
        Builds an ARX configuration object from a dictionary.

        Args:
            json_config (dict): Configuration data for ARX.

        Returns:
            Configured ARX configuration object.
        """
        arx_config = build_basic_configuration()
        arx_config = set_data_as_csv(arx_config, dataset)

        print(arx_config)   

        for attr in json_config["attributes"]:
            configure_attribute(
                arx_config,
                attr["key"],
                attr["key"],
                attr["type"],
                attr.get("weight"),
            )
        return arx_config

    def perform_risk_analysis(self, dataset: pd.DataFrame, json_config: dict):
        """
        Performs risk analysis on the dataset.

        Args:
            dataset (pd.DataFrame): Dataset to analyze.
            json_config (dict): Configuration for ARX.

        Returns:
            tuple: The result of the risk analysis including:
                - initial_highest_prosecutor
                - initial_average_prosecutor
                - quasi_identifiers
                - risk_assessment_server_answer

        Raises:
            ValueError: If the input dataset or JSON configuration is invalid.
            RuntimeError: If any step in the risk analysis process fails.
        """
        try:
            # Validate inputs
            if not isinstance(dataset, pd.DataFrame):
                raise ValueError("The dataset must be a pandas DataFrame.")
            if not isinstance(json_config, dict):
                raise ValueError("The configuration must be a dictionary.")

            # Build configuration
            try:
                arx_config = self.build_config_from_dict(json_config, dataset)
            except Exception as e:
                raise RuntimeError(f"Failed to build ARX configuration: {e}")


            # Apply risk assessment
            print("applying asessment")
            try:
                risk_assessment_server_answer = apply_assessment(
                    self.host, arx_config
                )
            except Exception as e:
                raise RuntimeError(f"Risk assessment failed: {e}")

            # Parse risk assessment
            try:
                (
                    initial_highest_prosecutor,
                    initial_average_prosecutor,
                    quasi_identifiers,
                ) = parse_risk_assessment(risk_assessment_server_answer)
            except Exception as e:
                raise RuntimeError(f"Failed to parse risk assessment: {e}")

            # Return results
            return (
                initial_highest_prosecutor,
                initial_average_prosecutor,
                quasi_identifiers,
                risk_assessment_server_answer,
            )

        except Exception as e:
            # Log or re-raise for debugging
            raise RuntimeError(f"Risk analysis process encountered an error: {e}")
