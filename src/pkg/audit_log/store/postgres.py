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

    def get_logs(self, offset: int, limit: int, filters: dict = {}, sort_by: str = None) -> list[AuditLog]:
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
        
        filter_conditions = []
        query_params = {'offset': offset, 'limit': limit}

        if 'userid' in filters:
            filter_conditions.append("a.userid = :userid")
            query_params['userid'] = filters['userid']
        if 'service' in filters:
            filter_conditions.append("a.service = :service")
            query_params['service'] = filters['service']
        if 'action' in filters:
            filter_conditions.append("a.action = :action")
            query_params['action'] = filters['action']
        if 'body' in filters:
            filter_conditions.append("a.body = :body")
            query_params['body'] = filters['body']
        if 'response' in filters:
            filter_conditions.append("a.response = :response")
            query_params['response'] = filters['response']
        if 'error' in filters:
            filter_conditions.append("a.error = :error")
            query_params['error'] = filters['error']
        if 'created_at' in filters:
            filter_conditions.append("a.created_at = :created_at")
            query_params['created_at'] = filters['created_at']

        if filter_conditions:
            query += " WHERE " + " AND ".join(filter_conditions)

        if sort_by:
            query += f" ORDER BY {sort_by}"
        else:
            query += " ORDER BY a.created_at"

        query += " OFFSET :offset LIMIT :limit;"

        with self.session_scope() as session:
            logs = session.execute(text(query), query_params).mappings().fetchall()

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
        
        filter_conditions = ["a.userid = :userid"]
        query_params = {'userid': id, 'offset': offset, 'limit': limit}

        if 'service' in filters:
            filter_conditions.append("a.service = :service")
            query_params['service'] = filters['service']
        if 'action' in filters:
            filter_conditions.append("a.action = :action")
            query_params['action'] = filters['action']
        if 'body' in filters:
            filter_conditions.append("a.body = :body")
            query_params['body'] = filters['body']
        if 'response' in filters:
            filter_conditions.append("a.response = :response")
            query_params['response'] = filters['response']
        if 'error' in filters:
            filter_conditions.append("a.error = :error")
            query_params['error'] = filters['error']
        if 'created_at' in filters:
            filter_conditions.append("a.created_at = :created_at")
            query_params['created_at'] = filters['created_at']

        if filter_conditions:
            query += " AND " + " AND ".join(filter_conditions)

        if sort_by:
            query += f" ORDER BY {sort_by}"
        else:
            query += " ORDER BY a.created_at"

        query += " OFFSET :offset LIMIT :limit;"
        
        with self.session_scope() as session:
            logs = session.execute(text(query), query_params).mappings().fetchall()

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
