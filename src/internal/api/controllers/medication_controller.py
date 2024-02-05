from server_template.models import TemplatebackendCreateMedicationReply
from server_template.models import TemplatebackendCreateMedicationResult
from server_template.models import TemplatebackendCreateMedicationRequest
from server_template.models import TemplatebackendDeleteMedicationReply
from server_template.models import TemplatebackendDeleteMedicationResult
from server_template.models import TemplatebackendGetMedicationReply
from server_template.models import TemplatebackendGetMedicationResult
from server_template.models import TemplatebackendListMedicationReply
from server_template.models import TemplatebackendListMedicationResult

import src.internal.api.controllers.converter.medication as medication_converter


class MedicationController:
    def __init__(self, config, medication_service):
        self.config = config
        self.medication_service = medication_service

    def medication_service_create_medication(self, user, body: TemplatebackendCreateMedicationRequest):
        medication = medication_converter.medication_to_business(body.medication)
        medication.userid = user.id
        medication.tenantid = user.tenantid

        m = self.medication_service.create_medication(medication)

        return TemplatebackendCreateMedicationReply(TemplatebackendCreateMedicationResult(m.id))

    def medication_service_delete_medication(self, user, id: str):
        return TemplatebackendDeleteMedicationReply(TemplatebackendDeleteMedicationResult())

    def medication_service_list_medication(self, user, id: int):
        # medication = TemplatebackendMedication()

        return TemplatebackendGetMedicationReply(TemplatebackendGetMedicationResult())

    def medication_service_list_medication(self, user, offset: int=None, limit: int=None):
        medications = self.medication_service.list_medications(user.tenantid, user.id, offset, limit)
        ms = [medication_converter.medication_from_business(m) for m in medications]
        return TemplatebackendListMedicationReply(TemplatebackendListMedicationResult(ms))
