import copy
from vyper import v
import jsonpickle # pip install jsonpickle
import json

conf = None

def provide_config(config_path: str):
    global conf
    if conf is None:
        conf = Config(config_path)

    return conf

def dict_to_class(d, class_name="Config"):
    """
    Convert a dictionary into a class recursively, handling nested dictionaries and lists.
    
    Args:
        d (dict): Dictionary to be converted.
        class_name (str): Name of the class.
        
    Returns:
        Type: A new class type initialized with the dictionary values.
    """

    # Create a new class with the specified name
    new_class = type(class_name, (), {})

    for k, v in d.items():
        if isinstance(v, dict):  # Check if the value is another dictionary
            setattr(new_class, k, dict_to_class(v, k.capitalize()))
        elif isinstance(v, list):  # Check if the value is a list
            setattr(new_class, k, [dict_to_class(item, class_name + k.capitalize()) if isinstance(item, dict) else item for item in v])
        else:
            setattr(new_class, k, v)
            
    return new_class

def dump_config(obj, level=0):
    if hasattr(obj, "__dict__"):
        for key, value in obj.__dict__.items():
            if key[0] != "_":
                if hasattr(value, "__dict__"):
                    print(" " * level + "{}:".format(key))
                    dump_config(value, level + 2)
                else:
                    print(" " * level + "{}: {}".format(key, value))


class Config:
    def __init__(self, config_path: str = "./configs/dev/template_backend.yml"):
        v.set_config_name('template_backend')
        v.set_config_file(config_path)
        v.set_config_type("yaml")
        v.read_in_config()

        self._config = v.all_settings()
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

        self._set_default("storage.description", "Type can be 'postgres'")
        self._set_default("storage.datastores.template_backend.type", "postgres")
        self._set_default("storage.datastores.template_backend.host", "localhost")
        self._set_default("storage.datastores.template_backend.port", "26257")
        self._set_default("storage.datastores.template_backend.username", "root")
        self._set_default("storage.datastores.template_backend.database", "template_backend")
        self._set_default("storage.datastores.template_backend.max_connections", 5000)
        self._set_default("storage.datastores.template_backend.max_lifetime", 0)
        self._set_default("storage.datastores.template_backend.ssl.enabled", False)
        self._set_default("storage.datastores.template_backend.ssl.certificate_file", "/template_backend/postgres-certs/client.crt")
        self._set_default("storage.datastores.template_backend.ssl.key_file", "/template_backend/postgres-certs/client.key")
        self._set_default("storage.datastores.template_backend.debug_mode", False)

    def config(self):
        return dict_to_class(copy.deepcopy(self._config))


