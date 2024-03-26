from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager

from src.pkg.audit_log.model.audit_log import AuditLog

class AuditLogStore:
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

    def log_event(self, audit_log: AuditLog):
        audit_log_query = """
INSERT INTO audit_log
    (userid, service, action, body, response, error, created_at)
VALUES
    (:userid, :service, :action, :body, :response, :error, :created_at);
"""
        with self.session_scope() as session:
            try:
                result = session.execute(text(audit_log_query), {
                    'userid': audit_log.userid,
                    'service':audit_log.service,
                    'action': audit_log.action,
                    'body': audit_log.body,
                    'response': audit_log.response,
                    'error': audit_log.error,
                    'created_at': audit_log.created_at
                }).fetchone()
                audit_id = result[0]

            except SQLAlchemyError as e:
                raise e

            return AuditLog(id=audit_id)

    def get_logs(self,offset:int,limit:int) -> list[AuditLog]:
        query = "SELECT * FROM audit_log ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            logs = session.execute(text(query),{
                'offset': offset,
                'limit': limit,
            }).mappings().fetchall()

            result = [
                AuditLog(
                    id=log.id,
                    userid=log.userid,
                    service=log.service,
                    action=log.action,
                    body=log.body,
                    response=log.response,
                    error=log.error,
                    created_at=log.createdat
                ) for log in logs
            ]
            return result

    def get_logs_for_user(self, id:str | int,offset:int,limit:int) -> list[AuditLog]:
        query = "SELECT * FROM audit_log WHERE userid = :userid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            logs = session.execute(text(query), {
                'userid': id,
                'offset':offset,
                'limit':limit
            }).mappings().fetchall()

            result = [
                AuditLog(
                    id=log.id,
                    userid=log.userid,
                    service=log.service,
                    action=log.action,
                    body=log.body,
                    response=log.response,
                    error=log.error,
                    created_at=log.createdat
                ) for log in logs
            ]
            return result
