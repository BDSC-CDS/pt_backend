from src.pkg.audit_log.model.audit_log import AuditLog

class AuditLogService:
    def __init__(self, audit_log_store):
        self.audit_log_store = audit_log_store

    def log_event(self, log: AuditLog):
        self.audit_log_store.log_event(log)

    def get_logs(self,offset:int,limit:int):
        logs = self.audit_log_store.get_logs(offset,limit)
        return logs

    def get_logs_for_user(self, identifier:int,offset:int,limit:int):
        logs = self.audit_log_store.get_logs_for_user(identifier=identifier,offset=offset,limit=limit)
        return logs
