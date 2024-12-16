import requests
import json
import pandas as pd


def executePOSTRequest(domain_and_port, url, body):
    response = requests.post(
        f"{domain_and_port}{url}",
        json=body,
        headers={"Content-Type": "application/json"},
    )
    return response.json()


def executeGETrequest(domain_and_port, url):
    full_url = f"{domain_and_port}{url}"
    response = requests.get(full_url)

    response_json_text = response.text
    result = json.loads(response_json_text)
    return result


def apply_expert_by_marketer_risk_level(domain_and_port, config):
    body_dict = {}

    # Add fields to body_dict if they exist
    if config.MARKETER_RISK is not None:
        body_dict["MARKETER_RISK"] = config.MARKETER_RISK
    if config.SUPPRESSION_LIMIT is not None:
        body_dict["SUPPRESSION_LIMIT"] = config.SUPPRESSION_LIMIT
    if config.NB_SOLUTIONS is not None:
        body_dict["NB_SOLUTIONS"] = config.NB_SOLUTIONS
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL
    # Fix hierarchy processing
    if config.HIERARCHIES is not None:
        body_dict["HIERARCHIES"] = {
            name: [{"V1": item["V1"], "V2": item["V2"]} for item in hierarchy]
            for name, hierarchy in config.HIERARCHIES.items()
        }

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

    return executePOSTRequest(
        domain_and_port, "deidentification/expert/marketer-risk-level", body_dict
    )


def apply_expert_by_highest_prosecutor_risk_level(domain_and_port, config):
    body_dict = {}

    # Add fields to body_dict if they exist
    if config.HIGHEST_PROSECUTOR_RISK is not None:
        body_dict["HIGHEST_PROSECUTOR_RISK"] = config.HIGHEST_PROSECUTOR_RISK
    if config.SUPPRESSION_LIMIT is not None:
        body_dict["SUPPRESSION_LIMIT"] = config.SUPPRESSION_LIMIT
    if config.NB_SOLUTIONS is not None:
        body_dict["NB_SOLUTIONS"] = config.NB_SOLUTIONS
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL
    # Fix hierarchy processing
    if config.HIERARCHIES is not None:
        body_dict["HIERARCHIES"] = {
            name: [{"V1": item["V1"], "V2": item["V2"]} for item in hierarchy]
            for name, hierarchy in config.HIERARCHIES.items()
        }

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

    return executePOSTRequest(
        domain_and_port,
        "deidentification/expert/highest-prosecutor-risk-level",
        body_dict,
    )


def apply_expert_by_average_prosecutor_risk_level(domain_and_port, config):
    body_dict = {}

    # Add fields to body_dict if they exist
    if config.HIGHEST_PROSECUTOR_RISK is not None:
        body_dict["HIGHEST_PROSECUTOR_RISK"] = config.HIGHEST_PROSECUTOR_RISK
    if config.SUPPRESSION_LIMIT is not None:
        body_dict["SUPPRESSION_LIMIT"] = config.SUPPRESSION_LIMIT
    if config.NB_SOLUTIONS is not None:
        body_dict["NB_SOLUTIONS"] = config.NB_SOLUTIONS
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL
    # Fix hierarchy processing
    if config.HIERARCHIES is not None:
        body_dict["HIERARCHIES"] = {
            name: [{"V1": item["V1"], "V2": item["V2"]} for item in hierarchy]
            for name, hierarchy in config.HIERARCHIES.items()
        }

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

    return executePOSTRequest(
        domain_and_port,
        "deidentification/expert/average-prosecutor-risk-level",
        body_dict,
    )


def apply_expert_by_privacy_models(domain_and_port, config):
    body_dict = {}
    if config.PRIVACY_MODELS:
        body_dict["PRIVACY_MODELS"] = config.PRIVACY_MODELS
    if config.SUPPRESSION_LIMIT:
        body_dict["SUPPRESSION_LIMIT"] = config.SUPPRESSION_LIMIT
    if config.NB_SOLUTIONS:
        body_dict["NB_SOLUTIONS"] = config.NB_SOLUTIONS
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL
    if config.HIERARCHIES:
        body_dict["HIERARCHIES"] = config.HIERARCHIES
    body_dict.update(
        {
            "ATTRIBUTES": config.ATTRIBUTES,
            "SRC": config.SRC,
            "DATA": config.DATA,
            "JDBC_CONNECTION_PARAMS": config.JDBC_CONNECTION_PARAMS,
        }
    )

    body_json = json.dumps(body_dict)
    return executePOSTRequest(
        domain_and_port, "deidentification/expert/privacy-models", body_json
    )


def apply_safe_harbor(domain_and_port, config):
    body_dict = {}
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL

    body_dict.update(
        {
            "SAFE_HARBOR_ATTRIBUTES": config.SAFE_HARBOR_ATTRIBUTES,
            "ATTRIBUTES": config.ATTRIBUTES,
            "SRC": config.SRC,
            "DATA": config.DATA,
            "JDBC_CONNECTION_PARAMS": config.JDBC_CONNECTION_PARAMS,
        }
    )

    body_json = json.dumps(body_dict)
    return executePOSTRequest(
        domain_and_port, "deidentification/safe-harbor", body_json
    )


def apply_expert_internal_chuv_context(domain_and_port, config):
    body_dict = {}
    if config.SUPPRESSION_LIMIT:
        body_dict["SUPPRESSION_LIMIT"] = config.SUPPRESSION_LIMIT
    if config.NB_SOLUTIONS:
        body_dict["NB_SOLUTIONS"] = config.NB_SOLUTIONS
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL
    if config.HIERARCHIES:
        body_dict["HIERARCHIES"] = config.HIERARCHIES
    body_dict.update(
        {
            "ATTRIBUTES": config.ATTRIBUTES,
            "SRC": config.SRC,
            "DATA": config.DATA,
            "JDBC_CONNECTION_PARAMS": config.JDBC_CONNECTION_PARAMS,
        }
    )

    body_json = json.dumps(body_dict)
    return executePOSTRequest(
        domain_and_port, "deidentification/expert/internal-chuv", body_json
    )


def apply_expert_multicentric_context(domain_and_port, config):
    body_dict = {}
    if config.SUPPRESSION_LIMIT:
        body_dict["SUPPRESSION_LIMIT"] = config.SUPPRESSION_LIMIT
    if config.NB_SOLUTIONS:
        body_dict["NB_SOLUTIONS"] = config.NB_SOLUTIONS
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL
    if config.HIERARCHIES:
        body_dict["HIERARCHIES"] = config.HIERARCHIES
    body_dict.update(
        {
            "ATTRIBUTES": config.ATTRIBUTES,
            "SRC": config.SRC,
            "DATA": config.DATA,
            "JDBC_CONNECTION_PARAMS": config.JDBC_CONNECTION_PARAMS,
        }
    )

    body_json = json.dumps(body_dict)
    return executePOSTRequest(
        domain_and_port, "deidentification/expert/multicentric", body_json
    )


def apply_expert_publication_context(domain_and_port, config):
    body_dict = {}
    if config.SUPPRESSION_LIMIT:
        body_dict["SUPPRESSION_LIMIT"] = config.SUPPRESSION_LIMIT
    if config.NB_SOLUTIONS:
        body_dict["NB_SOLUTIONS"] = config.NB_SOLUTIONS
    if config.IS_USED_POPULATION_MODEL is not None:
        body_dict["IS_USED_POPULATION_MODEL"] = config.IS_USED_POPULATION_MODEL
    if config.HIERARCHIES:
        body_dict["HIERARCHIES"] = config.HIERARCHIES
    body_dict.update(
        {
            "ATTRIBUTES": config.ATTRIBUTES,
            "SRC": config.SRC,
            "DATA": config.DATA,
            "JDBC_CONNECTION_PARAMS": config.JDBC_CONNECTION_PARAMS,
        }
    )

    body_json = json.dumps(body_dict)
    return executePOSTRequest(
        domain_and_port, "deidentification/expert/publication", body_json
    )


def code(domain_and_port, config):
    body_dict = {
        "ATTRIBUTES": config.ATTRIBUTES,
        "SRC": config.SRC,
        "DATA": config.DATA,
        "JDBC_CONNECTION_PARAMS": config.JDBC_CONNECTION_PARAMS,
    }

    body_json = json.dumps(body_dict)
    return executePOSTRequest(domain_and_port, "deidentification/code", body_json)


def decode(domain_and_port, config):
    body_dict = {
        "ATTRIBUTES": config.ATTRIBUTES,
        "KEY": config.KEY,
        "SRC": config.SRC,
        "DATA": config.DATA,
        "JDBC_CONNECTION_PARAMS": config.JDBC_CONNECTION_PARAMS,
    }

    body_json = json.dumps(body_dict)
    return executePOSTRequest(domain_and_port, "deidentification/decode", body_json)
