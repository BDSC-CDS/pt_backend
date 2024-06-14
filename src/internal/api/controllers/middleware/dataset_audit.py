from server_template.models import TemplatebackendDataset
from server_template.models import TemplatebackendStoreDatasetReply
from server_template.models import TemplatebackendStoreDatasetRequest

from  server_template.models import TemplatebackendGetDatasetContentReply
from  server_template.models import TemplatebackendGetDatasetMetadataReply
from  server_template.models import TemplatebackendListDatasetsReply

from src.internal.api.controllers.dataset_controller import DatasetController
from src.internal.util.interface.implements import implements_interface
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService

class DatasetControllerAudit():
    def __init__(self, next: DatasetController,auditLogService: AuditLogService):
        self.next = next
        self.auditLogService = auditLogService
        implements_interface(DatasetController, DatasetControllerAudit)

    def dataset_service_store_dataset(self, user, body:TemplatebackendStoreDatasetRequest): #TODO what is in user?
        body_serialized = f"user id: {user.id or ''}, dataset_name: {body.dataset_name or ''}"

        try:
            response : TemplatebackendStoreDatasetReply =  self.next.dataset_service_store_dataset(user, body)
            response_serialized = response.result.id
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="stored dataset",body=body_serialized,response=response_serialized))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error storing dataset",body=body_serialized,response=e, error=True))
            raise e

    def dataset_service_delete_dataset(self, user, name:str):
        try:
            response =  self.next.dataset_service_delete_dataset(user, name)
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="deleted dataset "+name, response=response))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error deleting dataset "+ name, response=e, error=True))
            raise e


    def dataset_service_get_dataset_metadata(self, user, name: str):
        try:
            response : TemplatebackendGetDatasetMetadataReply =  self.next.dataset_service_get_dataset_metadata(user, name)
            final_response = response.metadata.metadata
            response_serialized = f"dataset id: {final_response.dataset_id or ''}, column id: {final_response.column_id or ''}, type: {final_response.type or ''}"

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed metadata of dataset "+ name, response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing metadata of dataset "+ name, response=e, error=True))
            raise e

    # TODO cette méthode va pas
    def dataset_service_get_dataset_content(self, user, name: str, offset: int=None, limit: int=None):
        try:
            response : TemplatebackendGetDatasetContentReply =  self.next.dataset_service_get_dataset_content(user, name,offset,limit)
            response_serialized = f"dataframe: {response.result.dataframe or ''}"

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed content of dataset "+ name, response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing content of dataset "+ name, response=e, error=True))
            raise e

    def dataset_service_list_datasets(self, user, offset: int=None, limit: int=None):
        try:
            response : TemplatebackendListDatasetsReply =  self.next.dataset_service_list_datasets(user,offset,limit)
            response_serialized = f"number of datasets: {response.result.datasets.length or ''}"

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed list of datasets for user of size "+ response.result.datasets.length, response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing list of datasets for user of size"+ response.result.datasets.length, response=e, error=True))
            raise e
