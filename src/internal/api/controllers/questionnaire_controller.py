from server_template.models import TemplatebackendCreateReplyReply
from server_template.models import TemplatebackendCreateReplyRequest
from server_template.models import TemplatebackendCreateReplyResult
from server_template.models import TemplatebackendGetReplyReply
from server_template.models import TemplatebackendGetReplyResult
from server_template.models import TemplatebackendListRepliesReply
from server_template.models import TemplatebackendListRepliesResult
from server_template.models import TemplatebackendCreateQuestionnaireReply
from server_template.models import TemplatebackendCreateQuestionnaireResult
from server_template.models import TemplatebackendCreateQuestionnaireRequest
from server_template.models import TemplatebackendCreateQuestionnaireVersionReply
from server_template.models import TemplatebackendCreateQuestionnaireVersionResult
from server_template.models import TemplatebackendCreateQuestionnaireVersionRequest
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

    def questionnaire_service_create_reply(self, user, body: TemplatebackendCreateReplyRequest):
        reply = questionnaire_converter.reply_to_business(body.reply)
        r = self.questionnaire_service.create_reply(user, reply)
        return TemplatebackendCreateReplyReply(TemplatebackendCreateReplyResult(id=r.id))
    
    def questionnaire_service_list_replies(self, user, offset: int=None, limit: int=None):
        replies = self.questionnaire_service.list_replies(user, offset, limit)
        rs = [questionnaire_converter.reply_from_business(r) for r in replies]
        return TemplatebackendListRepliesReply(TemplatebackendListRepliesResult(replies=rs))

    def questionnaire_service_get_reply(self, user, id: int):
        reply = self.questionnaire_service.get_reply(user, id)
        r = questionnaire_converter.reply_from_business(reply)
        print("r", reply, r)
        return TemplatebackendGetReplyReply(TemplatebackendGetReplyResult(r))

    def questionnaire_service_create_questionnaire(self, user, body: TemplatebackendCreateQuestionnaireRequest):
        questionnaire = questionnaire_converter.questionnaire_to_business(body.questionnaire)
        questionnaire.userid = user.id
        questionnaire.tenantid = user.tenantid

        m = self.questionnaire_service.create_questionnaire(questionnaire)

        return TemplatebackendCreateQuestionnaireReply(TemplatebackendCreateQuestionnaireResult(m.id))
    
    def questionnaire_service_create_questionnaire_version(self, user, body: TemplatebackendCreateQuestionnaireVersionRequest):
        version = questionnaire_converter.questionnaire_version_to_business(body.version)
        # version.userid = user.id
        # version.tenantid = user.tenantid

        m = self.questionnaire_service.create_questionnaire_version(user, body.id, version)

        return TemplatebackendCreateQuestionnaireReply(TemplatebackendCreateQuestionnaireResult(m.id))

    def questionnaire_service_delete_questionnaire(self, user, id: str):
        return TemplatebackendDeleteQuestionnaireReply(TemplatebackendDeleteQuestionnaireResult())

    def questionnaire_service_get_questionnaire(self, user, id: int):
        questionnaire = self.questionnaire_service.get_questionnaire(user.tenantid, user, id)
        ms = questionnaire_converter.questionnaire_from_business(questionnaire)
        return TemplatebackendListQuestionnaireReply(TemplatebackendGetQuestionnaireResult(ms))

        # return TemplatebackendGetQuestionnaireReply(TemplatebackendGetQuestionnaireResult())

    def questionnaire_service_list_questionnaire(self, user, offset: int=None, limit: int=None):
        questionnaires = self.questionnaire_service.list_questionnaires(user.tenantid, user.id, offset, limit)
        ms = [questionnaire_converter.questionnaire_from_business(m) for m in questionnaires]
        return TemplatebackendListQuestionnaireReply(TemplatebackendListQuestionnaireResult(ms))
    

