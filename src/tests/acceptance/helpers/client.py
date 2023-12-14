import openapi_client
from openapi_client.models.templatebackend_create_user_reply import TemplatebackendCreateUserReply
from openapi_client.models.templatebackend_user import TemplatebackendUser
from openapi_client.rest import ApiException

def client():
    configuration = openapi_client.Configuration(
        host = "http://127.0.0.1:5000"
    )
    api_client = openapi_client.ApiClient(configuration)
    return api_client