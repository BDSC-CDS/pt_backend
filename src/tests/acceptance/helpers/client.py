import openapi_client
from src.tests.acceptance.helpers.jwt import jwt_token_admin

def client():
    configuration = openapi_client.Configuration(
        host = "http://127.0.0.1:5000"
    )
    api_client = openapi_client.ApiClient(configuration)
    return api_client

def admin_client():
    configuration = openapi_client.Configuration(
        host = "http://127.0.0.1:5000",
        api_key = {'Bearer': jwt_token_admin()}, # key is the name of the security scheme in the generated openapi.yaml
        api_key_prefix = {'Bearer': 'Bearer'},
    )
    api_client = openapi_client.ApiClient(configuration)
    return api_client