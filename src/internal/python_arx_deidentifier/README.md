# Python package for ARX Deidentifier


This repository provides a Python-based client for configuring, managing, and executing de-identification operations on sensitive datasets using various privacy models and risk levels. The client supports data sources in csv, and facilitates interactions with a de-identification server through HTTP requests.

## Features

- **Configuration of Privacy Models**: Define multiple privacy models to be applied to the dataset.
- **Risk Level Management**: Set marketer, highest prosecutor, and average prosecutor risk levels.
- **Attribute Management**: Define and configure attributes, hierarchies, and safe harbor categories.
- **Data Source Integration**: Load data from CSV or Oracle database sources.
- **Data Encoding & Decoding**: Encode and decode de-identified data.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library

Install required libraries:

```bash
pip install requests pandas
```

## Usage

### 1. Configuration Setup

Use `client.py` to create a basic configuration and set up dataset parameters.

Example:
```python
from client import build_basic_configuration, set_data_as_csv, configure_attribute

# Initialize configuration
config = build_basic_configuration()

# Set data source as CSV
dataset = pd.read_csv('path/to/dataset.csv')
config = set_data_as_csv(config, dataset)

# Configure an attribute
config = configure_attribute(config, 'Dataset1', 'Name', 'IDENTIFYING', 0.5)
```

### 2. Apply De-identification Models

Use `deidentificationClient.py` to apply specific de-identification methods based on the configured risk levels or privacy models.

Example:
```python
from deidentificationClient import apply_expert_by_marketer_risk_level

# Apply de-identification based on marketer risk level
response = apply_expert_by_marketer_risk_level('http://localhost:8080', config)
print(response)
```

### Available Functions

#### `client.py`

- `build_basic_configuration()`: Initializes a new configuration with default settings.
- `set_data_as_csv(config, dataset)`: Sets the dataset from a CSV file.
- `configure_attribute(config, dataset_name, arx_name, attribute_type, weight)`: Adds an attribute with details.
- `add_privacy_model(config, model_name, model_params, model_involved_attribute)`: Adds a privacy model to the configuration.

#### `deidentificationClient.py`

- `apply_expert_by_marketer_risk_level(domain_and_port, config)`: Applies de-identification based on the marketer risk level.
- `apply_expert_by_highest_prosecutor_risk_level(domain_and_port, config)`: Applies de-identification based on the highest prosecutor risk level.
- `apply_safe_harbor(domain_and_port, config)`: Applies de-identification based on safe harbor guidelines.
- `code(domain_and_port, config)`: Encodes the dataset.
- `decode(domain_and_port, config)`: Decodes the encoded dataset.

## Contributing

If you’d like to contribute, please fork the repository and make changes as you'd like. Pull requests are welcome.

---

This README provides an overview of the setup, usage, and functionality of your repo based on the provided files. Let me know if there’s anything more specific you’d like to include!