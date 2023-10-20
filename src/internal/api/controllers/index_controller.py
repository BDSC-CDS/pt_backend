import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from inspect import getmembers, isfunction


from server_template.models.index_service_create_hello_request import IndexServiceCreateHelloRequest
from server_template.models.rpc_status import RpcStatus
from server_template.models.templatebackend_create_hello_reply import TemplatebackendCreateHelloReply
from server_template.models.templatebackend_get_hello_reply import TemplatebackendGetHelloReply
from server_template import util

def index_service_create_hello(identifier: int, body: IndexServiceCreateHelloRequest):
    return TemplatebackendCreateHelloReply("hello"), 200


def index_service_get_hello():
    return TemplatebackendGetHelloReply("hello"), 200


def index_service_get_helloo():
    return TemplatebackendGetHelloReply("hello"), 200
