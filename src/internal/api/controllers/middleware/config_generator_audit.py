from server_template.models import TemplatebackendConfig
from server_template.models import TemplatebackendGetConfigsReply
from server_template.models import TemplatebackendCreateConfigReply
from server_template.models import TemplatebackendDeleteConfigReply
from server_template.models import TemplatebackendExportConfigReply

from src.internal.api.controllers.config_generator_controller import ConfigGeneratorController
from src.internal.util.interface.implements import implements_interface
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService
from src.pkg.config_generator.model.config_generator import ConfigGenerator

class ConfigGeneratorControllerAudit():
    def __init__(self, next: ConfigGeneratorController,auditLogService: AuditLogService):
        self.next = next
        self.auditLogService = auditLogService
        implements_interface(ConfigGeneratorController, ConfigGeneratorControllerAudit)

    def config_service_get_configs(self, user):

        try:
            response : TemplatebackendGetConfigsReply =  self.next.config_service_get_configs(user)
            response_serialized = ", ".join(str(config) for config in response.result.config)
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="accessed their configurations",response=(response_serialized or "")))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="error accessing their configurations",body="",response=e,error=True))
            raise e

    def config_service_create_config(self, user,body: TemplatebackendConfig):
        body_serialized = (
            f"id: {body.id or ''}, "
            f"questionnaire id: {body.questionnaireid or ''}, "
            f"hasScrambleField: {body.has_scramble_field or ''}, "
            f"has_date_shift: {body.has_date_shift or ''}, "
            f"hassub_field_list: {body.hassub_field_list or ''}, "
            f"hassub_field_regex: {body.hassub_field_regex or ''}, "
            f"scramble_field_fields: {' '.join(body.scramble_field_fields) if isinstance(body.scramble_field_fields, list) else (body.scramble_field_fields or '')}, "
            f"date_shift_lowrange: {body.date_shift_lowrange or ''}, "
            f"date_shift_highrange: {body.date_shift_highrange or ''}, "
            f"sub_field_list_field: {' '.join(body.sub_field_list_field) if isinstance(body.sub_field_list_field, list) else (body.sub_field_list_field or '')}, "
            f"sub_field_list_substitute: {' '.join(body.sub_field_list_substitute) if isinstance(body.sub_field_list_substitute, list) else (body.sub_field_list_substitute or '')}, "
            f"sub_field_regex_field: {' '.join(body.sub_field_regex_field) if isinstance(body.sub_field_regex_field, list) else (body.sub_field_regex_field or '')}, "
            f"sub_field_list_replacement: {body.sub_field_list_replacement or ''}, "
            f"sub_field_regex_regex: {body.sub_field_regex_regex or ''}, "
            f"sub_field_regex_replacement: {body.sub_field_regex_replacement or ''}, "
            f"created_at: {body.created_at or ''}"
        )


        try:
            response : TemplatebackendCreateConfigReply =  self.next.config_service_create_config(user,body)
            response_serialized = response.result.id
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="created configuration",body=body_serialized,response=(response_serialized or "")))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="error creating configurations",body=body_serialized,response=e,error=True))
            raise e

    def config_service_delete_config(self, user, id:int):
        try:
            response : TemplatebackendDeleteConfigReply =  self.next.config_service_delete_config(user, id)
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="deleted config "+str(id)+ ": ", response=response.result.success))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="Error deleting config "+ str(id), response=e, error=True))
            raise e

    def config_service_export_config(self,user,id:int):
        try:
            response : TemplatebackendExportConfigReply =  self.next.config_service_export_config(user, id)
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="exported config "+str(id)+ ": ", response=response.config))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="config generator", userid=user.id,action="Error exporting config "+ str(id), response=e, error=True))
            raise e
