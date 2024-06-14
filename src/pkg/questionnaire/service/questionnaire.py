from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.authentication.helper import helper

class QuestionnaireService:
    def __init__(self, questionnaire_store):
        self.questionnaire_store = questionnaire_store

    def get_questionnaire(self, tenantid: int, userid: int, id: int) -> Questionnaire:
        return self.questionnaire_store.get_questionnaire(tenantid, userid, id)
    
    def create_questionnaire(self, questionnaire: Questionnaire) -> Questionnaire:
        return self.questionnaire_store.create_questionnaire(questionnaire)
    
    def list_questionnaires(self, tenantid: int, userid: int, offset: int, limit: int) -> Questionnaire:
        questionnaires = self.questionnaire_store.list_questionnaires(tenantid, userid, offset, limit)

        return questionnaires