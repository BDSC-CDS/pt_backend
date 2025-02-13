from server_template.models import QuestionnaireServiceShareReplyRequest
from server_template.models import TemplatebackendCreateReplyRequest
from server_template.models import TemplatebackendCreateQuestionnaireRequest
from server_template.models import TemplatebackendCreateQuestionnaireVersionRequest
from src.internal.api.controllers.questionnaire_controller import QuestionnaireServiceController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class QuestionnaireServiceControllerAuthentication():
    def __init__(self, next: QuestionnaireServiceController):
        self.next = next
        implements_interface(QuestionnaireServiceControllerAuthentication, QuestionnaireServiceController)

    def questionnaire_service_create_reply(self, user, body: TemplatebackendCreateReplyRequest):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_create_reply(user, body)
    
    def questionnaire_service_list_replies(self, user, offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_list_replies(user, offset, limit)

    def questionnaire_service_get_reply(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_get_reply(user, id)

    def questionnaire_service_create_questionnaire(self, user, body: TemplatebackendCreateQuestionnaireRequest):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_create_questionnaire(user, body)
    
    def questionnaire_service_create_questionnaire_version(self, user, body: TemplatebackendCreateQuestionnaireVersionRequest):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_create_questionnaire_version(user, body)

    def questionnaire_service_delete_questionnaire(self, user, id: str):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_delete_questionnaire(user, id)

    def questionnaire_service_get_questionnaire(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_get_questionnaire(user, id)

    def questionnaire_service_list_questionnaire(self, user, offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_list_questionnaire(user, offset, limit)
    
    def questionnaire_service_share_reply(self, user, id: int, body: QuestionnaireServiceShareReplyRequest):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.questionnaire_service_share_reply(user, id, body)