import pandas as pd
from client.configuration_client import (
    build_basic_configuration,
    set_data_as_csv,
    set_nb_solutions,
    set_suppression_limit,
    set_is_used_population_model,
    configure_attribute,
    add_hierarchy,
    set_highest_prosecutor_risk,
)
from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment


class RiskAssessmentService:
    def __init__(self, arx_client, dataset_path, gender_hierarchy_path):
        self.arx_client = arx_client
        self.dataset_path = dataset_path
        self.gender_hierarchy_path = gender_hierarchy_path

    def get_risk_assessment(self, tenantid: int, userid: int) -> RiskAssessment:
        # Step 1: Fetch all records
        records = self.arx_client.get_all_records()

        # Step 2: Perform risk assessment based on the provided logic
        risk_assessment_result = self.perform_risk_analysis(records)

        # Step 3: Return the RiskAssessment object
        return risk_assessment_result

    def perform_risk_analysis(self, records):
        """
        Perform risk analysis using the provided logic.
        """
        # Step 1: Build the basic configuration
        config = build_basic_configuration()

        # Step 2: Load the dataset and set it in the configuration
        dataset = pd.read_csv(self.dataset_path, header=0, sep=";")
        dataset = dataset.astype(str)
        config = set_data_as_csv(config, dataset)

        # Step 3: Configure the job parameters
        config = set_nb_solutions(config, 2)
        config = set_suppression_limit(config, 0.5)
        config = set_is_used_population_model(config, False)

        # Step 4: Configure attributes
        config = configure_attribute(
            config, "IPP_MASTER", "IPP_MASTER", "IDENTIFYING_ATTRIBUTE", None
        )
        config = configure_attribute(
            config, "NUMERO_SEJOUR", "NUMERO_SEJOUR", "IDENTIFYING_ATTRIBUTE", None
        )
        config = configure_attribute(
            config, "DATE_ENTREE_SEJOUR", "DATE_ENTREE_SEJOUR", "INSENSITIVE_ATTRIBUTE", None
        )
        config = configure_attribute(config, "NOM", None, "IDENTIFYING_ATTRIBUTE", None)
        config = configure_attribute(config, "PRENOM", None, "IDENTIFYING_ATTRIBUTE", None)
        config = configure_attribute(
            config, "DATE NAISSANCE", "DATE_NAISSANCE", "INSENSITIVE_ATTRIBUTE", None
        )
        config = configure_attribute(config, "SEXE", "SEXE", "QUASI_IDENTIFYING_ATTRIBUTE", 0.5)
        config = configure_attribute(
            config, "NATIONALITE", "NATIONALITE", "INSENSITIVE_ATTRIBUTE", 0.5
        )
        config = configure_attribute(
            config, "DATE DECES CHUV", "DATE_DECES_CHUV", "INSENSITIVE_ATTRIBUTE", 0.5
        )

        # Step 5: Add hierarchies for attributes
        hierarchy_data = pd.read_csv(self.gender_hierarchy_path, header=None, sep=";")
        config = add_hierarchy(config, "SEXE", hierarchy_data)

        # Step 6: Set the highest prosecutor risk
        config = set_highest_prosecutor_risk(config, 0.5)

        # Step 7: Return the processed configuration as a mock RiskAssessment
        # Here we assume a transformation of `config` into `RiskAssessment` is needed.
        return RiskAssessment(config)
