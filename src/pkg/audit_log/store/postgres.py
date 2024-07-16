from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.user.model.user import User

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
    (:userid, :service, :action, :body, :response, :error, NOW())
RETURNING id;
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
                }).fetchone()
                audit_id = result[0]

            except SQLAlchemyError as e:
                raise e

            return AuditLog(id=audit_id)

    def get_logs(self, offset: int, limit: int, filters: dict = None, sort_by: str = None) -> list[AuditLog]:
        query = """
            SELECT
                a.id, a.userid, a.service, 
                a.action, a.body, a.response, 
                a.error, a.created_at,
                u.username as username, 
                u.firstname as firstname, 
                u.lastname as lastname 
            FROM audit_log a
            LEFT JOIN users u ON a.userid = u.id
        """
        
        if filters:
            filter_conditions = " AND ".join([f"{key} = :{key}" for key in filters.keys()])
            query += f" WHERE {filter_conditions}"

        if sort_by:
            query += f" ORDER BY {sort_by}"
        else:
            query += " ORDER BY created_at"

        query += " OFFSET :offset LIMIT :limit;"
        
        with self.session_scope() as session:
            logs = session.execute(text(query), {**filters, 'offset': offset, 'limit': limit}).mappings().fetchall()

            result = [
                AuditLog(
                    id=log.id,
                    userid=log.userid,
                    service=log.service,
                    action=log.action,
                    body=log.body,
                    response=log.response,
                    error=log.error,
                    created_at= log.created_at,
                    user=User(
                        id=log.userid,
                        username=log.username,
                        firstname=log.firstname,
                        lastname=log.lastname,
                    )
                ) for log in logs
            ]
            return result

    def get_logs_for_user(self, id: int, offset: int, limit: int, filters: dict = None, sort_by: str = None) -> list[AuditLog]:
        query = """
            SELECT
                a.id, a.userid, a.service, 
                a.action, a.body, a.response, 
                a.error, a.created_at,
                u.username as username, 
                u.firstname as firstname, 
                u.lastname as lastname 
            FROM audit_log a
            LEFT JOIN users u ON a.userid = u.id
            WHERE a.userid = :userid
        """
        
        if filters:
            filter_conditions = " AND ".join([f"{key} = :{key}" for key in filters.keys()])
            query += f" AND {filter_conditions}"

        if sort_by:
            query += f" ORDER BY {sort_by}"
        else:
            query += " ORDER BY created_at"

        query += " OFFSET :offset LIMIT :limit;"
        
        with self.session_scope() as session:
            logs = session.execute(text(query), {**filters, 'userid': id, 'offset': offset, 'limit': limit}).mappings().fetchall()

            result = [
                AuditLog(
                    id=log.id,
                    userid=log.userid,
                    service=log.service,
                    action=log.action,
                    body=log.body,
                    response=log.response,
                    error=log.error,
                    created_at=log.created_at,
                    user=User(
                        id=log.userid,
                        username=log.username,
                        firstname=log.firstname,
                        lastname=log.lastname,
                    )
                ) for log in logs
            ]
            return result
