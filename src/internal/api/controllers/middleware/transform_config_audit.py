from server_template.models import TemplatebackendCreateTransformConfigRequest
from server_template.models import TemplatebackendListTransformConfigsReply
from server_template.models import TemplatebackendCreateTransformConfigReply
from server_template.models import TemplatebackendDeleteTransformConfigReply
from server_template.models import TemplatebackendExportTransformConfigReply
from controllers.transform_config_controller import TransformConfigServiceController
from src.internal.util.interface.implements import implements_interface
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService


class TransformConfigServiceControllerAudit():
    def __init__(self, next: TransformConfigServiceController,auditLogService: AuditLogService):
        self.next = next
        self.auditLogService = auditLogService
        implements_interface(TransformConfigServiceController, TransformConfigServiceControllerAudit)

    def transform_config_service_create_transform_config(self, user, body: TemplatebackendCreateTransformConfigRequest):
        body_serialized = (
            f"id: {body.config.id or ''}, "
            f"questionnaire id: {body.config.questionnaireid or ''}, "
            f"config name: {body.config.name or ''}, "
            f"date_shift: {body.config.date_shift.lowrange or ''}, {body.config.date_shift.highrange or ''}, "
            f"scramble_field: {' '.join(body.config.scramble_field.fields)}, "
            f"sub_field_list_name: {' '.join(subfield.name for subfield in body.config.sub_field_list_list)}, "
            f"sub_field_regex_name: {' '.join(subfield.name for subfield in body.config.sub_field_regex_list)}, "
        )

        try:
            response : TemplatebackendCreateTransformConfigReply = self.next.transform_config_service_create_transform_config(user,body)
            response_serialized = response.result.id
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="created configuration",body=body_serialized,response=(response_serialized or "")))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="Error creating configurations",body=body_serialized,response=e,error=True))
            raise e
        
    def transform_config_service_list_transform_configs(self, user, offset: int=None, limit: int=None):
        try:
            response : TemplatebackendListTransformConfigsReply =  self.next.transform_config_service_list_transform_configs(user, offset, limit)
            response_serialized = ", ".join(str(config) for config in response.result.configs)
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="accessed their configurations",response=(response_serialized or "")))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="Error accessing their configurations",body="",response=e,error=True))
            raise e

    def transform_config_service_delete_transform_config(self, user, id:int):
        try:
            response : TemplatebackendDeleteTransformConfigReply =  self.next.transform_config_service_delete_transform_config(user, id)
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="deleted config "+str(id)+ ": ", response=response.result.success))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="Error deleting config "+ str(id), response=e, error=True))
            raise e

    def transform_config_service_export_transform_config(self,user,id:int):
        try:
            response : TemplatebackendExportTransformConfigReply =  self.next.transform_config_service_export_transform_config(user, id)
            if type(response) is tuple and response[1] == 404:
                response_serialized = "Does not exist"
            else:
                response_serialized = response.config
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="exported config "+str(id)+ ": ", response=response_serialized))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="Error exporting config "+ str(id), response=e, error=True))
            raise e

    def transform_config_service_export_transform_config_json(self, user, id:int):
        try:
            response = self.next.transform_config_service_export_transform_config_json(user, id)
            
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="downloaded json of config "+str(id)+ ": ", response=""))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="transform config", userid=user.id,action="Error downloading json of config "+ str(id), response=e, error=True))
            raise e
