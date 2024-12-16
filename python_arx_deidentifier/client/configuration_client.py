import requests
import json
import pandas as pd


class Configuration:
    def __init__(self):
        self.DATA = pd.DataFrame()
        self.JDBC_CONNECTION_PARAMS = {}
        self.ATTRIBUTES = pd.DataFrame(
            columns=["datasetName", "arxName", "attributeType", "weight"]
        )
        self.PRIVACY_MODELS = []
        self.HIERARCHIES = {}
        self.SAFE_HARBOR_ATTRIBUTES = {}
        self.SRC = ""
        self.KEY = ""
        self.NB_SOLUTIONS = 0
        self.SUPPRESSION_LIMIT = 0.5
        self.MARKETER_RISK = 0.0
        self.HIGHEST_PROSECUTOR_RISK = 0.0
        self.AVERAGE_PROSECUTOR_RISK = 0.0
        self.IS_USED_POPULATION_MODEL = False


class PrivacyModel:
    def __init__(self, name, params, involved_attribute):
        self.name = name
        self.params = pd.DataFrame(params)
        self.involved_attribute = involved_attribute


def build_basic_configuration():
    new_config = Configuration()
    new_config.JDBC_CONNECTION_PARAMS = {}
    new_config.PRIVACY_MODELS = []
    new_config.HIERARCHIES = {}
    new_config.SAFE_HARBOR_ATTRIBUTES = {}
    return new_config


def execute_post_request(domain_and_port, url, body):
    response = requests.post(
        f"{domain_and_port}{url}",
        json=body,
        headers={"Content-Type": "application/json"},
    )
    return response.json()


def execute_get_request(domain_and_port, url):
    response = requests.get(f"{domain_and_port}{url}")
    return response.json()


def set_data_as_csv(config, dataset):
    # Ensure that missing values (e.g., empty strings or 'nan' strings) are properly converted to NaN
    dataset.replace(
        {"": float("nan"), "nan": float("nan")}, inplace=True
    )  # Replaces empty and 'nan' strings with NaN

    # Now replace NaN values with empty strings
    config.DATA = dataset.applymap(
        lambda x: "" if pd.isna(x) else str(x)
    )  # Replace NaN with empty string

    config.SRC = "csv"
    return config


def set_data_as_oracle_params(
    config, input_url, input_username, input_password, table_name
):
    config.JDBC_CONNECTION_PARAMS = {
        "url": input_url,
        "username": input_username,
        "password": input_password,
        "table": table_name,
    }
    config.SRC = "oracle"
    return config


def configure_attribute(config, dataset_name, arx_name, attribute_type, weight):
    config.ATTRIBUTES = config.ATTRIBUTES.append(
        {
            "datasetName": dataset_name,
            "arxName": arx_name,
            "attributeType": attribute_type,
            "weight": weight,
        },
        ignore_index=True,
    )
    return config


def add_hierarchy(config, name, hierarchy_df):
    # Convert the DataFrame to a list of dictionaries with V1 and V2 keys
    hierarchy_list = [
        {"V1": row[0], "V2": row[1]} for row in hierarchy_df.values.tolist()
    ]
    config.HIERARCHIES[name] = hierarchy_list
    return config


def set_nb_solutions(config, nb_solutions):
    config.NB_SOLUTIONS = nb_solutions
    return config


def set_suppression_limit(config, suppression_limit):
    config.SUPPRESSION_LIMIT = suppression_limit
    return config


def set_marketer_risk(config, marketer_risk):
    config.MARKETER_RISK = marketer_risk
    return config


def set_highest_prosecutor_risk(config, highest_prosecutor_risk):
    config.HIGHEST_PROSECUTOR_RISK = highest_prosecutor_risk
    return config


def set_average_prosecutor_risk(config, average_prosecutor_risk):
    config.AVERAGE_PROSECUTOR_RISK = average_prosecutor_risk
    return config


def add_privacy_model(config, model_name, model_params, model_involved_attribute):
    privacy_model = PrivacyModel(model_name, model_params, model_involved_attribute)
    config.PRIVACY_MODELS.append(privacy_model)
    return config


def set_is_used_population_model(config, is_used_population_model):
    config.IS_USED_POPULATION_MODEL = is_used_population_model
    return config


def add_attribute_to_safe_harbor_category(config, category, attribute):
    if category not in config.SAFE_HARBOR_ATTRIBUTES:
        config.SAFE_HARBOR_ATTRIBUTES[category] = []
    config.SAFE_HARBOR_ATTRIBUTES[category].append(attribute)
    return config


def set_key(config, key):
    config.KEY = key
    return config


def to_json_privacy_models(privacy_models):
    result = []
    for privacy_model in privacy_models:
        model_dict = {
            "name": privacy_model.name,
            "params": [
                {"name": row["name"], "value": row["value"]}
                for _, row in privacy_model.params.iterrows()
            ],
            "involvedAttribute": privacy_model.involved_attribute,
        }
        result.append(model_dict)
    return json.dumps(result)
