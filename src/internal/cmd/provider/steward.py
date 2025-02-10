from src.internal.steward import steward
from src.internal.cmd.provider import config, user, questionnaire

steward_instance = None

def provide_steward():
    global steward_instance
    if steward_instance is None:
        conf = config.provide_config()
        users_service = user.provide_users_service()
        questionnaire_service = questionnaire.provide_questionnaire_service()

        steward_instance = steward.Steward(conf.steward, users_service, questionnaire_service)
        
    return steward_instance