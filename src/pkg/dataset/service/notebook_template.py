# %% [markdown]
# # De-identification using the ARX service template
# 
# This notebook is a template to perform de-identification using the ARX service.

# %% [markdown]
# ### Imports 

# %% 
import pandas as pd
import requests
from py_arx.assessment_client import apply_assessment
from py_arx.deidentification_client import apply_expert_by_average_prosecutor_risk_level
from py_arx.configuration_client import (
    build_basic_configuration,
    set_data_as_csv,
    set_nb_solutions,
    set_suppression_limit,
    set_is_used_population_model,
    configure_attribute,
    add_hierarchy,
    set_average_prosecutor_risk,
)

# %% [markdown]
# ### Parameters

# %%
token = "{{token}}"
arx_service_url = "{{arx_service_url}}"
backend_host = "{{backend_public_url}}"

# Alternatively to get the token you can authenticate
# username = "{{username}}"
# password = "<your password here>"
# response = requests.post(backend_host + "/api/rest/v1/authentication/login", json={"username":username, "password":password})
# token = response.json()["result"]["token"]

# %% [markdown]
# ### Fill the dataset

# %%
dataset = pd.read_parquet(
    backend_host + "/api/v1/dataset/dataframe/{{datasetid}}", 
    storage_options={"Authorization":"Bearer " + token}
)
dataset = dataset.astype(str)
dataset

# %% [markdown]
# ### configuration

# %%
############### Build the basic configuration ################

config = build_basic_configuration()
config = set_data_as_csv(config, dataset)

################ Fill the job parameters values ################

config = set_nb_solutions(config, 2)
config = set_suppression_limit(config, 1)
config = set_is_used_population_model(config, False)

################ Fill the attributes ################

config = configure_attribute(
    config, "IPP_MASTER", "IPP_MASTER", "IDENTIFYING_ATTRIBUTE", None
)

# DATE_ENTREE_SEJOUR

# Quasi-identifying attributes to generalize

config = configure_attribute(
    config, "DATE NAISSANCE", "DATE_NAISSANCE", "INSENSITIVE_ATTRIBUTE", None
)
config = configure_attribute(config, "SEXE", "SEXE", "QUASI_IDENTIFYING_ATTRIBUTE", 0.5)
config = configure_attribute(
    config, "NATIONALITE", "NATIONALITE", "QUASI_IDENTIFYING_ATTRIBUTE", 0.5
)


################ Fill the hierarchies (optional for attributes managed by the service by default) ################
# config = add_hierarchy(
#     config, "SEXE", pd.read_csv("../gender_hierarchy.csv", header=None, sep=";")
# )

# %% [markdown]
# ### Execute de-identification

# %%
################ Execute de-identification by Marketer Risk Level ################
config = set_average_prosecutor_risk(config, 0.45)

# %%
apply_assessment(arx_service_url, config)

# %%
apply_expert_by_average_prosecutor_risk_level(arx_service_url, config)
