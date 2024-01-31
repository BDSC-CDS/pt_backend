import src.internal.api.server_template.controllers.medication_controller as connexion_medication_controller
import src.internal.api.controllers.medication_controller as internal_medication_controller
import src.internal.api.controllers.middleware.medication_authorization as medication_controller_authorization
# from src.pkg.medication.service.medication import MedicationService
# from src.pkg.medication.store.postgres import MedicationStore as PostgresMedicationStore
from .config import provide_config
from .db import provide_db_type, provide_db

medication_controller = None
medication_service = None
medication_store = None

def provide_medication_controller():
    global medication_controller

    if medication_controller is not None:
        return medication_controller

    controller = internal_medication_controller.MedicationController(provide_config(), provide_medication_service())
    controller = medication_controller_authorization.MedicationControllerAuthentication(controller)
    medication_controller = connexion_medication_controller.MedicationController(controller)

    return medication_controller

def provide_medication_service():
    global medication_service

    if medication_service is not None:
        return medication_service

    # medication_service = MedicationService(provide_medication_store())

    return medication_service

def provide_medication_store():
    global medication_store

    if medication_store is not None:
        return medication_store
    
    tpe = provide_db_type()

    if tpe == "postgres":
        # medication_store = PostgresMedicationStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")
        

    return medication_store