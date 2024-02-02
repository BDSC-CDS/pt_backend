from src.pkg.medication.model.medication import Medication
from server_template.models import TemplatebackendMedication

def medication_to_business(medication: TemplatebackendMedication) -> Medication:
    return Medication(
        id=medication.id,
        userid=medication.user_id,
        name=medication.name,
        dosage=medication.dosage,
        frequency=medication.frequency,
    )

def medication_from_business(medication: Medication) -> TemplatebackendMedication:
    return TemplatebackendMedication(
        id=medication.id,
        user_id=medication.userid,
        name=medication.name,
        dosage=medication.dosage,
        frequency=medication.frequency,
        created_at=medication.createdat,
        updated_at=medication.updatedat
    )
