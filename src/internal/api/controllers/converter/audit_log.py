from src.pkg.audit_log.model.audit_log import AuditLog
from server_template.models import TemplatebackendAuditLog
from .user import user_from_business, user_to_business

def audit_log_to_business(audit_log: TemplatebackendAuditLog) -> AuditLog:
    return AuditLog(
        id=audit_log.id,
        userid=audit_log.user_id,
        service=audit_log.service,
        action=audit_log.action,
        body=audit_log.body,
        response=audit_log.response,
        created_at=audit_log.created_at,
        error=audit_log.error,
        user=user_to_business(audit_log.user)
    )

def audit_logs_to_business(audit_logs: list[TemplatebackendAuditLog]) -> list[AuditLog]:
    return [audit_log_to_business(log) for log in audit_logs]

def audit_log_from_business(audit_log: AuditLog) -> TemplatebackendAuditLog:
    return TemplatebackendAuditLog(
        id=audit_log.id,
        userid=audit_log.userid,
        service=audit_log.service,
        action=audit_log.action,
        body=audit_log.body,
        response=audit_log.response,
        created_at=audit_log.created_at,
        user=user_from_business(audit_log.user.drop_sensitive_fields())
    )

def audit_logs_from_business(audit_logs: list[AuditLog]) -> list[TemplatebackendAuditLog]:
    return [audit_log_from_business(log) for log in audit_logs]