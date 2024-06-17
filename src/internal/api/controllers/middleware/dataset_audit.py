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
            print("response audit: ",response)
            response_serialized = response.result.id
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="stored dataset",body=body_serialized,response=response_serialized))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error storing dataset",body=body.dataset_name,response=e, error=True))
            raise e

    def dataset_service_delete_dataset(self, user, id:int):
        try:
            response : TemplatebackendDeleteDatasetReply =  self.next.dataset_service_delete_dataset(user, id)
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="deleted dataset "+str(id)+ ": ", response=response.result.success))
            return response
        except Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error deleting dataset "+ str(id), response=e, error=True))
            raise e


    def dataset_service_get_dataset_metadata(self, user, id: int):
        try:
            response : TemplatebackendGetDatasetMetadataReply =  self.next.dataset_service_get_dataset_metadata(user, id)
            print("RESPONE: ",response)
            if type(response) is tuple and response[1] == 404:
                final_response = []
            else:
                final_response = response.metadata.metadata

            response_serialized =[ f"dataset id: {r.dataset_id or ''}, column id: {r.column_id or ''}, type: {r.type or ''}" for r in final_response]

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed metadata of dataset "+ str(id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing metadata of dataset "+ str(id), response=e, error=True))
            raise e

    def dataset_service_get_dataset_content(self, user, id: int, offset: int=None, limit: int=None):
        try:
            response : TemplatebackendGetDatasetContentReply =  self.next.dataset_service_get_dataset_content(user, id,offset,limit)
            response_serialized = f"columns: {response.result.columns or ''}"

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed content of dataset "+ str(id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing content of dataset "+ str(id), response=e, error=True))
            raise e

    def dataset_service_list_datasets(self, user, offset: int=None, limit: int=None):
        try:
            response : TemplatebackendListDatasetsReply =  self.next.dataset_service_list_datasets(user,offset,limit)
            response_serialized = f"number of datasets: {str(len(response.result.datasets)) or ''}"

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed list of datasets for user of size "+ str(len(response.result.datasets)), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing list of datasets for user of size"+ str(len(response.result.datasets)), response=e, error=True))
            raise e
