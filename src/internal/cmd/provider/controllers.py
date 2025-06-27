from . import config
from .authentication import provide_authentication_controller
from .index import provide_index_controller
from .user import provide_user_controller
from .questionnaire import provide_questionnaire_controller
from .risk_assessment import provide_risk_assessment_controller
from .dataset import provide_dataset_controller
from .audit_log import provide_audit_log_controller
from .transform_config import provide_transform_config_controller
controllers = None

def provide_controllers():
    global controllers

    if controllers is not None:
        return controllers

    controllers = {}

    controllers['authentication_controller'] = provide_authentication_controller()
    controllers['index_controller'] = provide_index_controller()
    controllers['user_controller'] = provide_user_controller()
    controllers['questionnaire_controller'] = provide_questionnaire_controller()
    controllers['risk_assessment_controller'] = provide_risk_assessment_controller()
    controllers['dataset_controller'] = provide_dataset_controller()
    controllers['audit_log_controller'] = provide_audit_log_controller()
    controllers['transform_config_controller'] = provide_transform_config_controller()

    return controllers
