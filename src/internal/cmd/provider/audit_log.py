from flask import request, jsonify
from src.pkg.audit_log.service.audit_log import AuditLogService
from src.internal.cmd.provider.audit_log_provider import provide_audit_log_service

audit_log_service = provide_audit_log_service()

def get_logs_for_user(userid):
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=10, type=int)
    try:
        logs = audit_log_service.get_logs_for_user(userid, offset, limit)
        return jsonify({"logs": logs}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def log_event():
    data = request.json
    try:
        audit_log_service.log_event(
            userid=data['userid'],
            service=data['service'],
            action=data['action'],
            body=data['body'],
            response=data['response'],
            error=data['error']
        )
        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
