

from src.internal.clients.arx import client
from src.internal.clients.jupyterhub.client import JupyterhubClient
from .config import provide_config


arx_client = None
jupyterhub_client = None

def provide_arx_client():
    global arx_client
    if arx_client is not None:
        return arx_client

    arx_client = client.ArxClient(provide_config().clients.arx)
    return arx_client

def provide_jupyterhub_client():
    global jupyterhub_client

    if jupyterhub_client is not None:
        return jupyterhub_client

    jupyterhub_client = JupyterhubClient(provide_config().clients.jupyterhub)
    
    return jupyterhub_client
