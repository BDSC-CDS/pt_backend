import os
from src.internal.cmd.provider import config

def get_test_config():
    config_path = os.environ.get("TEST_CONFIG")
    conf = config.provide_config(config_path)
    return conf