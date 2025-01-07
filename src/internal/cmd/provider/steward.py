from src.internal.steward import steward
from src.internal.cmd.provider import config, user, questionnaire

steward_instance = None

def provide_steward():
    global steward_instance
    if steward_instance is None:
        conf = config.provide_config()
        user_service = user.provide_user_service()
        questionnaire_service = questionnaire.provide_questionnaire_service()

        steward_instance = steward.Steward(conf.steward, user_service, questionnaire_service)
        
    return steward_instance