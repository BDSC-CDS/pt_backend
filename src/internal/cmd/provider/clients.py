
from src.internal.clients.arx import client
from .config import provide_config


arx_client = None

def provide_arx_client():
    global arx_client
    if arx_client is not None:
        return arx_client

    arx_client = client.ArxClient(provide_config().clients.arx)
    return arx_client


