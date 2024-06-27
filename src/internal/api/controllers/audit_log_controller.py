from flask import Blueprint, request, jsonify
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService
from src.internal.cmd.provider.audit_log import provide_audit_log_service

audit_log_service = provide_audit_log_service()
audit_log_controller = Blueprint('audit_log_controller', __name__)

@audit_log_controller.route('/audit_log', methods=['POST'])
def add_audit_log():
    data = request.get_json()
    log = AuditLog(
        userid=data.get('userid'),
        service=data.get('service', ''),
        action=data.get('action', ''),
        body=data.get('body', ''),
        response=data.get('response', ''),
        created_at=data.get('created_at', datetime.datetime.utcnow().isoformat()),
        error=data.get('error', False)
    )
    audit_log_service.log_event(log)
    return jsonify({'success': True})

@audit_log_controller.route('/audit_logs', methods=['GET'])
def list_audit_logs():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    offset = (page - 1) * page_size
    logs = audit_log_service.get_logs(offset, page_size)
    return jsonify({'logs': [log.to_dict() for log in logs]})

@audit_log_controller.route('/audit_logs/user/<int:user_id>', methods=['GET'])
def list_user_audit_logs(user_id):
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    offset = (page - 1) * page_size
    logs = audit_log_service.get_logs_for_user(user_id, offset, page_size)
    return jsonify({'logs': [log.to_dict() for log in logs]})
