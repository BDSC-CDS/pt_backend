from server_template.models import TemplatebackendCreateMedicationRequest
from src.internal.api.controllers.medication_controller import MedicationController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class MedicationControllerAuthentication():
    def __init__(self, next: MedicationController):
        self.next = next
        implements_interface(MedicationController, MedicationControllerAuthentication)

    def medication_service_create_medication(self, user, body: TemplatebackendCreateMedicationRequest):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.medication_service_create_medication(user, body)

    def medication_service_delete_medication(self, user, id: str):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.medication_service_delete_medication(user, id)

    def medication_service_get_medication(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.medication_service_get_medication(user, id)

    def medication_service_list_medication(self, user, offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        
        return self.next.medication_service_list_medication(user, offset, limit)