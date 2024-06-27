from src.pkg.audit_log.model.audit_log import AuditLog
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class AuditLogORM(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=False)
    service = Column(String, nullable=False)
    action = Column(Text, nullable=False)
    body = Column(Text, nullable=True)
    response = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)
    error = Column(Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'userid': self.userid,
            'service': self.service,
            'action': self.action,
            'body': self.body,
            'response': self.response,
            'created_at': self.created_at.isoformat(),
            'error': self.error
        }

class AuditLogStore:
    def __init__(self, db):
        self.engine = db.engine  # Use the provided database engine
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def log_event(self, log: AuditLog):
        session = self.Session()
        log_orm = AuditLogORM(
            userid=log.userid,
            service=log.service,
            action=log.action,
            body=log.body,
            response=log.response,
            created_at=log.created_at,
            error=log.error
        )
        session.add(log_orm)
        session.commit()

    def get_logs(self, offset: int, limit: int):
        session = self.Session()
        logs = session.query(AuditLogORM).offset(offset).limit(limit).all()
        return logs

    def get_logs_for_user(self, identifier: int, offset: int, limit: int):
        session = self.Session()
        logs = session.query(AuditLogORM).filter(AuditLogORM.userid == identifier).offset(offset).limit(limit).all()
        return logs
