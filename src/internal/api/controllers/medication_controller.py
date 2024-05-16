# src/internal/api/controllers/medication_controller.py
from server_template.models import TemplatebackendCreateMedicationReply
from server_template.models import TemplatebackendCreateMedicationResult
from server_template.models import TemplatebackendCreateMedicationRequest
from server_template.models import TemplatebackendDeleteMedicationReply
from server_template.models import TemplatebackendDeleteMedicationResult
from server_template.models import TemplatebackendGetMedicationReply
from server_template.models import TemplatebackendGetMedicationResult
from server_template.models import TemplatebackendListMedicationReply
from server_template.models import TemplatebackendListMedicationResult

class MedicationController:
    def __init__(self, config, medication_service):
        self.config = config
        self.authentication_service = medication_service

    def medication_service_create_medication(self, user, body: TemplatebackendCreateMedicationRequest):
        return TemplatebackendCreateMedicationReply(TemplatebackendCreateMedicationResult())

    def medication_service_delete_medication(self, user, id: str):
        return TemplatebackendDeleteMedicationReply(TemplatebackendDeleteMedicationResult())

    def medication_service_get_medication(self, user, id: int):
        # medication = TemplatebackendMedication()

        return TemplatebackendGetMedicationReply(TemplatebackendGetMedicationResult())

    def medication_service_list_medication(self, user, offset: int=None, limit: int=None):
        return TemplatebackendListMedicationReply(TemplatebackendListMedicationResult())