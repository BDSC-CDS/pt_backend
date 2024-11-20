# src/pkg/risk_assessment/store/postgres.py

from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.risk_assessment.model.risk_assessment import RiskAssessment


class RiskAssessmentStore:
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

    def create_risk_assessment(self, risk_assessment: RiskAssessment) -> RiskAssessment:
        """
        Inserts a new risk assessment into the database.

        Args:
            risk_assessment (RiskAssessment): The risk assessment data to be inserted.

        Returns:
            RiskAssessment: The inserted risk assessment with its ID populated.
        """
        query = """
                INSERT INTO risk_assessment 
                    (tenantid, userid, dataset_id, risk_assessment)
                VALUES 
                    (:tenantid, :userid, :dataset_id, :risk_assessment) 
                RETURNING id;
                """

        with self.session_scope() as session:
            try:
                result = session.execute(
                    text(query),
                    {
                        "tenantid": risk_assessment.tenantid,
                        "userid": risk_assessment.userid,
                        "dataset_id": risk_assessment.dataset_id,
                        "risk_assessment": risk_assessment.risk_assessment,
                    },
                ).fetchone()
                risk_assessment_id = result[0]
            except SQLAlchemyError as e:
                raise e

            return RiskAssessment(
                id=risk_assessment_id,
                tenantid=risk_assessment.tenantid,
                userid=risk_assessment.userid,
                dataset_id=risk_assessment.dataset_id,
                risk_assessment=risk_assessment.risk_assessment,
            )

    def list_risk_assessments(
        self, tenantid: int, userid: int, offset: int, limit: int
    ) -> list[RiskAssessment]:
        """
        Retrieves a list of risk assessments for a given tenant and user.

        Args:
            tenantid (int): Tenant ID to filter by.
            userid (int): User ID to filter by.
            offset (int): Number of records to skip.
            limit (int): Maximum number of records to retrieve.

        Returns:
            list[RiskAssessment]: A list of risk assessments.
        """
        query = """
SELECT id, tenantid, userid, dataset_id, risk_assessment 
FROM risk_assessment 
WHERE tenantid = :tenantid AND userid = :userid 
ORDER BY id OFFSET :offset LIMIT :limit;
"""

        with self.session_scope() as session:
            risk_assessments = session.execute(
                text(query),
                {
                    "tenantid": tenantid,
                    "userid": userid,
                    "offset": offset,
                    "limit": limit,
                },
            ).mappings().fetchall()

            return [
                RiskAssessment(
                    id=ra.id,
                    tenantid=ra.tenantid,
                    userid=ra.userid,
                    dataset_id=ra.dataset_id,
                    risk_assessment=ra.risk_assessment,
                )
                for ra in risk_assessments
            ]
