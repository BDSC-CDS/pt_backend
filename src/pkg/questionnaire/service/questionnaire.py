from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.questionnaire.model.questionnaire import QuestionnaireVersion
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
    
    def list_questionnaires(self, tenantid: int, userid: int, offset: int, limit: int) -> Questionnaire:
        questionnaires = self.questionnaire_store.list_questionnaires(tenantid, userid, offset, limit)

        return questionnaires