from server_template.models import TemplatebackendDataset
from server_template.models import TemplatebackendStoreDatasetReply
from server_template.models import TemplatebackendStoreDatasetRequest

from  server_template.models import TemplatebackendGetDatasetContentReply
from  server_template.models import TemplatebackendGetDatasetMetadataReply
from  server_template.models import TemplatebackendListDatasetsReply
from  server_template.models import TemplatebackendDeleteDatasetReply
from  server_template.models import TemplatebackendTransformDatasetReply
from  server_template.models import TemplatebackendTransformDatasetRequest
from server_template.models import TemplatebackendRevertDatasetReply
from server_template.models import TemplatebackendRevertDatasetRequest
from server_template.models import TemplatebackendChangeTypesDatasetRequest
from server_template.models import TemplatebackendChangeTypesDatasetReply
from server_template.models import TemplatebackendGetDatasetInfoReply
from server_template.models import DatasetServiceUpdateDatasetNameRequest
from server_template.models import TemplatebackendUpdateDatasetNameReply
from src.internal.api.controllers.dataset_controller import DatasetServiceController
from src.internal.util.interface.implements import implements_interface
from src.pkg.audit_log.model.audit_log import AuditLog
from src.pkg.audit_log.service.audit_log import AuditLogService

class DatasetServiceControllerAudit():
    def __init__(self, next: DatasetServiceController,auditLogService: AuditLogService):
        self.next = next
        self.auditLogService = auditLogService
        implements_interface(DatasetServiceController, DatasetServiceControllerAudit)

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

    def dataset_service_get_dataset_info(self, user, id: int):
        try:
            response : TemplatebackendGetDatasetInfoReply =  self.next.dataset_service_get_dataset_info(user, id)

            response_serialized =  f"dataset id: {response.dataset.id or ''}"

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed info of dataset "+ str(id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing info of dataset "+ str(id), response=e, error=True))
            raise e
        
    def dataset_service_update_dataset_name(self, user, id: int, body:DatasetServiceUpdateDatasetNameRequest):
        try:
            response : TemplatebackendUpdateDatasetNameReply =  self.next.dataset_service_update_dataset_name(user, id, body)
            response_serialized = response.result.success or ''
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="updated name of dataset "+ str(id) + " to " + str(body.name), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error updating name of dataset "+ str(id) + " to " + str(body.name), response=e, error=True))
            raise e

    def dataset_service_get_dataset_metadata(self, user, id: int):
        try:
            response : TemplatebackendGetDatasetMetadataReply =  self.next.dataset_service_get_dataset_metadata(user, id)
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
        
    def dataset_service_get_dataset_csv(self, user, id: int, offset: int=None, limit: int=None):
        try:
            response =  self.next.dataset_service_get_dataset_csv(user, id, offset, limit)

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="downloaded csv of dataset "+ str(id), response=""))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error downloading content of dataset "+ str(id), response=e, error=True))
            raise e


    def dataset_service_get_dataset_dataframe(self, user, id: int, offset: int=None, limit: int=None):
        try:
            response =  self.next.dataset_service_get_dataset_dataframe(user, id,offset,limit)

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed dataframe of dataset "+ str(id), response=""))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing content of dataset "+ str(id), response=e, error=True))
            raise e
    
    def dataset_service_get_dataset_jupyterhub(self, user, id: int):
        try:
            response =  self.next.dataset_service_get_dataset_jupyterhub(user, id)

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed jupyterhub of dataset "+ str(id), response=""))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing content of dataset "+ str(id), response=str(e), error=True))
            raise e

    def dataset_service_get_dataset_identifier(self, user, id: int, offset: int=None, limit: int=None):
        try:
            response : TemplatebackendGetDatasetContentReply =  self.next.dataset_service_get_dataset_identifier(user, id,offset,limit)
            response_serialized = f"columns: {response.result.columns or ''}"

            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="accessed filtered content of dataset "+ str(id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error accessing filtered content of dataset "+ str(id), response=e, error=True))
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

    def dataset_service_transform_dataset(self, user, body:TemplatebackendTransformDatasetRequest):
        try:
            response : TemplatebackendTransformDatasetReply =  self.next.dataset_service_transform_dataset(user,body)
            response_serialized = response.result.id or ''
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="transformed dataset "+ str(body.dataset_id) + " with config " + str(body.config_id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error transforming dataset "+ str(body.dataset_id) + " with config " + str(body.config_id), response=e, error=True))
            raise e


    def dataset_service_revert_dataset(self, user, body:TemplatebackendRevertDatasetRequest):
        try:
            response : TemplatebackendRevertDatasetReply =  self.next.dataset_service_revert_dataset(user,body)
            response_serialized = response.id or ''
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="reverted dataset "+ str(body.id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error reverting dataset "+ str(body.id), response=e, error=True))
            raise e

    def dataset_service_change_types_dataset(self, user, body:TemplatebackendChangeTypesDatasetRequest):
        try:
            response : TemplatebackendChangeTypesDatasetReply =  self.next.dataset_service_change_types_dataset(user,body)
            response_serialized = response.id or ''
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="changed type of dataset "+ str(body.dataset_id), response=response_serialized))
            return response
        except  Exception as e:
            self.auditLogService.log_event(AuditLog(service="dataset", userid=user.id,action="Error changing type of dataset "+ str(body.dataset_id), response=e, error=True))
            raise e
