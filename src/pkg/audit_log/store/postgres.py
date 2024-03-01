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
    (userid, action, created_at)
VALUES
    (:userid, :action, :created_at);
"""
        with self.session_scope() as session:
            try:
                session.execute(text(audit_log_query), {
                    'userid': audit_log.userid,
                    'action': audit_log.action,
                    'created_at': audit_log.created_at
                })
            except SQLAlchemyError as e:
                raise e

    def get_logs(self):
        query = "SELECT * FROM audit_log;"
        with self.session_scope() as session:
            logs = session.execute(text(query)).fetchall()
            return logs

    def get_logs_for_user(self, id:str | int):
        query = "SELECT * FROM audit_log WHERE userid = :userid;"
        with self.session_scope() as session:
            logs = session.execute(text(query), {
                'userid': id,
            }).fetchall()

            return logs
