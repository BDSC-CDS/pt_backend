import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.index_service_create_hello_request import IndexServiceCreateHelloRequest  # noqa: E501
from openapi_server.models.rpc_status import RpcStatus  # noqa: E501
from openapi_server.models.templatebackend_create_hello_reply import TemplatebackendCreateHelloReply  # noqa: E501
from openapi_server.models.templatebackend_get_hello_reply import TemplatebackendGetHelloReply  # noqa: E501
from openapi_server import util


def index_service_create_hello(identifier, body):  # noqa: E501
    """Get a hello

    This endpoint returns a hello # noqa: E501

    :param identifier: 
    :type identifier: int
    :param body: 
    :type body: dict | bytes

    :rtype: Union[TemplatebackendCreateHelloReply, Tuple[TemplatebackendCreateHelloReply, int], Tuple[TemplatebackendCreateHelloReply, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = IndexServiceCreateHelloRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def index_service_get_hello():  # noqa: E501
    """Get a hello

    This endpoint returns a hello # noqa: E501


    :rtype: Union[TemplatebackendGetHelloReply, Tuple[TemplatebackendGetHelloReply, int], Tuple[TemplatebackendGetHelloReply, int, Dict[str, str]]
    """
    return 'do some magic!'


def index_service_get_helloo():  # noqa: E501
    """Get a hello

    This endpoint returns a hello # noqa: E501


    :rtype: Union[TemplatebackendGetHelloReply, Tuple[TemplatebackendGetHelloReply, int], Tuple[TemplatebackendGetHelloReply, int, Dict[str, str]]
    """
    return 'do some magic!'
