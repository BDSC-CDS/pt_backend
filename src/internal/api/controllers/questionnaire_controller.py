from server_template.models import TemplatebackendCreateQuestionnaireReply
from server_template.models import TemplatebackendCreateQuestionnaireResult
from server_template.models import TemplatebackendCreateQuestionnaireRequest
from server_template.models import TemplatebackendDeleteQuestionnaireReply
from server_template.models import TemplatebackendDeleteQuestionnaireResult
from server_template.models import TemplatebackendGetQuestionnaireReply
from server_template.models import TemplatebackendGetQuestionnaireResult
from server_template.models import TemplatebackendListQuestionnaireReply
from server_template.models import TemplatebackendListQuestionnaireResult

import src.internal.api.controllers.converter.questionnaire as questionnaire_converter


class QuestionnaireController:
    def __init__(self, config, questionnaire_service):
        self.config = config
        self.questionnaire_service = questionnaire_service

    def questionnaire_service_create_questionnaire(self, user, body: TemplatebackendCreateQuestionnaireRequest):
        questionnaire = questionnaire_converter.questionnaire_to_business(body.questionnaire)
        questionnaire.userid = user.id
        questionnaire.tenantid = user.tenantid

        m = self.questionnaire_service.create_questionnaire(questionnaire)

        return TemplatebackendCreateQuestionnaireReply(TemplatebackendCreateQuestionnaireResult(m.id))

    def questionnaire_service_delete_questionnaire(self, user, id: str):
        return TemplatebackendDeleteQuestionnaireReply(TemplatebackendDeleteQuestionnaireResult())

    def questionnaire_service_get_questionnaire(self, user, id: int):
        questionnaire = self.questionnaire_service.get_questionnaire(user.tenantid, user, id)
        ms = questionnaire_converter.questionnaire_from_business(questionnaire)
        return TemplatebackendListQuestionnaireReply(TemplatebackendListQuestionnaireResult(ms))

        # return TemplatebackendGetQuestionnaireReply(TemplatebackendGetQuestionnaireResult())

    def questionnaire_service_list_questionnaire(self, user, offset: int=None, limit: int=None):
        questionnaires = self.questionnaire_service.list_questionnaires(user.tenantid, user.id, offset, limit)
        ms = [questionnaire_converter.questionnaire_from_business(m) for m in questionnaires]
        return TemplatebackendListQuestionnaireReply(TemplatebackendListQuestionnaireResult(ms))