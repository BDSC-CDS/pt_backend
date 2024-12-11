from python_arx_deidentifier.client.assessment_client import apply_assessment
from python_arx_deidentifier.client.configuration_client import (
    build_basic_configuration,
    set_data_as_csv,
    set_nb_solutions,
    set_suppression_limit,
    set_is_used_population_model,
    configure_attribute,
)
from src.internal.clients.arx import client
from .config import provide_config
import pandas as pd 

arx_client = None

def provide_arx_client():
    global arx_client
    if arx_client is not None:
        return arx_client

    arx_client = client.ArxClient(provide_config().clients.arx)
    return arx_client

def build_config_from_dict(json_config: dict):
    """
    Builds an ARX configuration object from a dictionary.

    Args:
        json_config (dict): Configuration data for ARX.

    Returns:
        Configured ARX configuration object.
    """
    arx_config = build_basic_configuration()

    for attr in json_config["attributes"]:
        arx_config = configure_attribute(
            arx_config,
            attr["key"],
            attr.get("source"),
            attr["type"],
            attr.get("weight"),
        )
    return arx_config

def perform_risk_analysis(dataset: pd.DataFrame, json_config: dict, arx_client):
    """
    Performs risk analysis on the dataset.

    Args:
        dataset (pd.DataFrame): Dataset to analyze.
        json_config (dict): Configuration for ARX.
        arx_client: ARX client instance.

    Returns:
        The result of the risk analysis.
    """
    arx_config = build_config_from_dict(json_config)
    arx_config = set_data_as_csv(arx_config, dataset)
    return apply_assessment(arx_client, arx_config)
