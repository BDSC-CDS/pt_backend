from src.pkg.audit_log.model.audit_log import AuditLog
from server_template.models import TemplatebackendAuditLog

def audit_log_to_business(audit_log: TemplatebackendAuditLog) -> AuditLog:
    return AuditLog(
        id=audit_log.id,
        userid=audit_log.user_id,
        service=audit_log.service,
        action=audit_log.action,
        body=audit_log.body,
        response=audit_log.response,
        created_at=audit_log.created_at,
        error=audit_log.error
    )

def audit_log_from_business(audit_log: AuditLog) -> TemplatebackendAuditLog:
    return TemplatebackendAuditLog(
        id=audit_log.id,
        user_id=audit_log.userid,
        service=audit_log.service,
        action=audit_log.action,
        body=audit_log.body,
        response=audit_log.response,
        created_at=audit_log.createdat,
        updated_at=audit_log.updatedat
    )
