import copy

config = None

def inject_config():
    if config is not None:
        raise Exception("config already injected")
    
def config():
    if config is None:
        raise Exception("config not injected")
    
    return copy.deepcopy(config)