import requests
import pandas as pd


def executePOSTRequest(domain_and_port, url, body):
    response = requests.post(
        f"{domain_and_port}{url}",
        json=body,
        headers={"Content-Type": "application/json"},
    )
    return response.json()


def apply_assessment(domain_and_port, config):

    body_dict = {}

    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL

    if config.ATTRIBUTES is not None:
        # Process 'ATTRIBUTES' dynamically, excluding None values
        body_dict["ATTRIBUTES"] = []
        for _, row in config.ATTRIBUTES.iterrows():
            attribute = {}
            # Only include attributes with non-null values
            if pd.notna(row["datasetName"]):
                attribute["datasetName"] = row["datasetName"]
            if pd.notna(row["arxName"]):
                attribute["arxName"] = row["arxName"]
            if pd.notna(row["attributeType"]):
                attribute["attributeType"] = row["attributeType"]
            if pd.notna(row["weight"]):
                attribute["weight"] = row["weight"]

            # Add the attribute only if it contains any key-value pairs
            if attribute:
                body_dict["ATTRIBUTES"].append(attribute)

    if config.SRC is not None:
        body_dict["SRC"] = config.SRC

    if config.DATA is not None:

        # Handle the 'DATA' field dynamically
        if isinstance(config.DATA, pd.DataFrame):
            # Replace NaN values with ""
            body_dict["DATA"] = config.DATA.applymap(
                lambda x: (
                    ""
                    if pd.isna(x)
                    else (
                        int(float(x))
                        if isinstance(x, (float, int, str))
                        and str(x).replace(".", "", 1).isdigit()
                        else str(x)
                    )
                )
            ).to_dict(orient="records")
        else:
            # If it's not a DataFrame, use the data as is
            body_dict["DATA"] = config.DATA

    if isinstance(config.JDBC_CONNECTION_PARAMS, pd.DataFrame):
        body_dict["JDBC_CONNECTION_PARAMS"] = list(config.JDBC_CONNECTION_PARAMS)
    else:
        body_dict["JDBC_CONNECTION_PARAMS"] = list(config.JDBC_CONNECTION_PARAMS)

    return executePOSTRequest(domain_and_port, "assessment", body_dict)


def parse_risk_assessment(data):
    """
    Parses the risk assessment data to extract the initial highest prosecutor, initial average prosecutor, 
    and quasi-identifiers.

    Args:
        data (dict): The input dictionary containing risk assessment results.

    Returns:
        tuple: A tuple containing initial highest prosecutor (float), initial average prosecutor (float), 
               and a string listing quasi-identifiers.
    """
    try:
        # Extract the ID dynamically
        metadata = next(iter(data['resultsMetadata'].values()))
        risks = metadata['risks']
        initial_highest_prosecutor = risks['initialHighestProsecutor']
        initial_average_prosecutor = risks['initialAverageProsecutor']

        # Extract quasi-identifiers
        qis = metadata['attributeTypes']['quasiIdentifying']
        quasi_identifiers_str = f"quasi identifiers: {', '.join(qis)}"

        return initial_highest_prosecutor, initial_average_prosecutor, quasi_identifiers_str
    except KeyError as e:
        raise ValueError(f"Missing key in the data structure: {e}")