from src.pkg.medication.model.medication import Medication
from src.pkg.authentication.helper import helper

class MedicationService:
    def __init__(self, medication_store):
        self.medication_store = medication_store

    def create_medication(self, medication: Medication) -> Medication:
        return self.medication_store.create_medication(medication)
    
    def list_medications(self, tenantid: int, userid: int, offset: int, limit: int) -> Medication:
        medications = self.medication_store.list_medications(tenantid, userid, offset, limit)

        return medications