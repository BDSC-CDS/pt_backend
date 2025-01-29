import copy
from vyper import v
import os
import re

conf = None

def provide_config(config_path: str = "./configs/dev/pt_backend.yml"):
    global conf
    if conf is None:
        conf = Config(config_path)

    return conf.config()

def dict_to_class(d, class_name="Config"):
    """
    Convert a dictionary into a class recursively, handling nested dictionaries and lists.
    The class will also behave as a dictionary.
    
    Args:
        d (dict): Dictionary to be converted.
        class_name (str): Name of the class.
        
    Returns:
        Type: A new class type initialized with the dictionary values.
    """

    # Create a new class with the specified name, subclassing dict
    class_dict = type(class_name, (dict,), {})
    
    class_instance = class_dict()

    for k, v in d.items():
        if isinstance(v, dict):
            class_instance[k] = dict_to_class(v, k.capitalize())
        elif isinstance(v, list):
            class_instance[k] = [dict_to_class(item, class_name + k.capitalize()) if isinstance(item, dict) else item for item in v]
        else:
            class_instance[k] = v
        setattr(class_instance, k, class_instance[k])
            
    return class_instance

def dump_config(obj, level=0):
    if hasattr(obj, "__dict__"):
        for key, value in obj.__dict__.items():
            if key[0] != "_":
                if hasattr(value, "__dict__"):
                    print(" " * level + "{}:".format(key))
                    dump_config(value, level + 2)
                else:
                    print(" " * level + "{}: {}".format(key, value))

def replace_env_variables(d):
    """
    Recursively replace the placeholders in the format ${ENV_VARIABLE} with 
    their corresponding values from the environment variables.
    
    Args:
        d (dict or str): The input dictionary or string that may contain placeholders.
    
    Returns:
        dict or str: The dictionary or string with replaced environment variables.
    """
    if isinstance(d, dict):
        for key, value in d.items():
            d[key] = replace_env_variables(value)
    elif isinstance(d, list):
        for i in range(len(d)):
            d[i] = replace_env_variables(d[i])
    elif isinstance(d, str):
        # Replace ${ENV_VARIABLE} with the value of the environment variable
        d = re.sub(r'\${([A-Z_]+)}', lambda match: os.getenv(match.group(1), None) or match.group(0), d)
    
    return d

class Config:
    def __init__(self, config_path: str = "./configs/dev/pt_backend.yml"):
        self._config = {}

        if config_path != "":
            v.set_config_name('pt_backend')
            v.set_config_file(config_path)
            v.set_config_type("yaml")
            v.read_in_config()

            self._config = v.all_settings()
        # Replace env variables in the config values
        self._config = replace_env_variables(self._config)
        # Provide default values to empty config
        self._provide_defaults()

        dump_config(dict_to_class(self._config))

    def _set_default(self, k, v):
        ks = k.split(".")
        b = self._config
        for k in ks[:-1]:
            if b.get(k) is None:
                b[k] = {}
            b = b[k]
        if ks[-1] not in b:
            b[ks[-1]] = v
        

    def _provide_defaults(self):
        self._set_default("daemon.http.host", "127.0.0.1")
        self._set_default("daemon.http.port", "5000")
        self._set_default("daemon.jwt.secret", "eREH6oV#&6bX&zadL%")
        self._set_default("daemon.jwt.expiration_time", 72 * 60 * 60)
        self._set_default("daemon.jwt.max_renewal_amount", 24)
        self._set_default("daemon.public_url", "http://localhost:5000")

        self._set_default("clients.arx.host", "http://localhost:8080/")
        self._set_default("clients.jupyterhub.debug", False)

        self._set_default("storage.description", "Type can be 'postgres'")
        self._set_default("storage.datastores.pt_backend.type", "postgres")
        self._set_default("storage.datastores.pt_backend.driver", "psycopg2")
        self._set_default("storage.datastores.pt_backend.host", "localhost")
        self._set_default("storage.datastores.pt_backend.port", "26257")
        self._set_default("storage.datastores.pt_backend.username", "root")
        self._set_default("storage.datastores.pt_backend.database", "pt_backend")
        self._set_default("storage.datastores.pt_backend.max_connections", 5000)
        self._set_default("storage.datastores.pt_backend.max_lifetime", 0)
        self._set_default("storage.datastores.pt_backend.ssl.enabled", False)
        self._set_default("storage.datastores.pt_backend.ssl.certificate_file", "/pt_backend/postgres-certs/client.crt")
        self._set_default("storage.datastores.pt_backend.ssl.key_file", "/pt_backend/postgres-certs/client.key")
        self._set_default("storage.datastores.pt_backend.debug_mode", False)

    def config(self):
        return dict_to_class(copy.deepcopy(self._config))