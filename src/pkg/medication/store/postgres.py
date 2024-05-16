# src/pkg/medication/store/postgres.py

from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.medication.model.medication import Medication


class MedicationStore:
    def __init__(self, db: Engine):
        self.db = db

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        Session = sessionmaker(bind=self.db)
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_medication(self, medication: Medication) -> Medication:
        medication_query = """
INSERT INTO medication 
    (tenantid, userid, name, dosage, frequency)
VALUES 
    (:tenantid, :userid, :name, :dosage, :frequency) 
RETURNING id;
"""

        with self.session_scope() as session:
            try:
                result = session.execute(text(medication_query), {
                    'tenantid': medication.tenantid,
                    'userid': medication.userid,
                    'name': medication.name,
                    'dosage': medication.dosage,
                    'frequency': medication.frequency,
                }).fetchone()
                medication_id = result[0]

            except SQLAlchemyError as e:
                raise e

            return Medication(id=medication_id)
    
    def list_medications(self, tenantid: int, userid: int, offset: int, limit: int) -> list[Medication] :
        query = "SELECT * FROM medication where tenantid = :tenantid and userid = :userid order by createdat offset :offset limit :limit;"
        with self.session_scope() as session:
            medications = session.execute(text(query), {
                'tenantid': tenantid,
                'userid': userid,
                'offset': offset,
                'limit': limit,
            }).mappings().fetchall()

            ms = [
                Medication(
                    id=medication.id,

                    tenantid=medication.tenantid,
                    userid=medication.userid,

                    name=medication.name,
                    dosage=medication.dosage,
                    frequency=medication.frequency,

                    createdat=medication.createdat,
                    updatedat=medication.updatedat
                ) for medication in medications
            ]

            return ms
