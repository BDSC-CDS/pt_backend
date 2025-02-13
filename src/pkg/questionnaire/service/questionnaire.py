from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.questionnaire.model.questionnaire import QuestionnaireVersion
from src.pkg.questionnaire.model.questionnaire import Reply
from src.pkg.questionnaire.model.questionnaire import QuestionReply
from src.pkg.authentication.helper import helper
from src.pkg.user.model.user import User

class QuestionnaireService:
    def __init__(self, questionnaire_store):
        self.questionnaire_store = questionnaire_store

    def get_questionnaire(self, tenantid: int, userid: int, id: int) -> Questionnaire:
        return self.questionnaire_store.get_questionnaire(tenantid, userid, id)
    
    def create_questionnaire(self, questionnaire: Questionnaire) -> Questionnaire:
        return self.questionnaire_store.create_questionnaire(questionnaire)
    
    def create_questionnaire_version(self, user: User, questionnaire_id:int, version: QuestionnaireVersion) -> QuestionnaireVersion:
        return self.questionnaire_store.create_questionnaire_version(user.tenantid, user.id, questionnaire_id, version)
        # return self.questionnaire_store.create_questionnaire(questionnaire_id, version)
    
    def list_questionnaires(self, tenantid: int, userid: int, offset: int = 0, limit: int = None) -> Questionnaire:
        questionnaires = self.questionnaire_store.list_questionnaires(tenantid, userid, offset, limit)
        return questionnaires
    
    def create_reply(self, user:User, reply: Reply) -> Reply:
        # TODO check if reply complies to q version
        return self.questionnaire_store.create_reply(user.tenantid, user.id, reply)
    
    def get_reply(self, user, reply_id: int) -> Reply:
        return self.questionnaire_store.get_reply(user.tenantid, user.id, reply_id)
    
    def list_replies(self, user, offset: int=None, limit: int=None) -> list[Reply]:
        return self.questionnaire_store.list_replies(user.tenantid, user.id, offset, limit)
    
    def create_share(self, user, reply_id: int, sharedwith_userid: int):
        questionnaire_reply = self.questionnaire_store.get_reply(user.tenantid, user.id, reply_id)
        if questionnaire_reply is None or questionnaire_reply.userid != user.id:
            return False
        
        return self.questionnaire_store.create_share(user.tenantid, user.id, reply_id, sharedwith_userid)
