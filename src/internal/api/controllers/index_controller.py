from server_template.models.index_service_create_hello_request import IndexServiceCreateHelloRequest
from server_template.models.templatebackend_create_hello_reply import TemplatebackendCreateHelloReply
from server_template.models.templatebackend_get_hello_reply import TemplatebackendGetHelloReply

class IndexController():
    def index_service_create_hello(self, user, identifier: int, body: IndexServiceCreateHelloRequest):
        return TemplatebackendCreateHelloReply("hello"), 200


    def index_service_get_hello(self, user):
        if user is None:
            return TemplatebackendGetHelloReply("hello"), 200

        return TemplatebackendGetHelloReply("hello " + user.firstname), 200
        