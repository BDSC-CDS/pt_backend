from server_template.models import TemplatebackendDataset
from server_template.models import TemplatebackendStoreDatasetRequest
from server_template.models import TemplatebackendTransformDatasetRequest
from server_template.models import TemplatebackendRevertDatasetRequest
from server_template.models import TemplatebackendChangeTypesDatasetRequest
from src.internal.api.controllers.dataset_controller import DatasetServiceController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class DatasetServiceControllerAuthentication():
    def __init__(self, next: DatasetServiceController):
        self.next = next
        implements_interface(DatasetServiceController, DatasetServiceControllerAuthentication)

    def dataset_service_store_dataset(self, user, body: TemplatebackendStoreDatasetRequest):
        if not is_authenticated(user): # TODO is_self ? comment on vérifie que qu'il accède a son propre dataset ?
            return None, 403
        return self.next.dataset_service_store_dataset(user, body)

    def dataset_service_delete_dataset(self, user,id:int):
        # if not is_admin_or_self(user, id):
        #     return None, 403
        # TODO remettre ?
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_delete_dataset(user, id)

    def dataset_service_get_dataset_info(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_info(user, id)

    def dataset_service_get_dataset_metadata(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_metadata(user, id)

    def dataset_service_get_dataset_content(self, user, id: int,offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_content(user, id, offset, limit)
    
    def dataset_service_get_dataset_dataframe(self, user, id: int,offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_dataframe(user, id, offset, limit)
    
    def dataset_service_get_dataset_jupyterhub(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_jupyterhub(user, id)

    def dataset_service_get_dataset_identifier(self, user, id: int,offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_identifier(user, id,offset,limit)

    def dataset_service_list_datasets(self, user, offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_list_datasets(user, offset,limit)

    def dataset_service_transform_dataset(self, user, body:TemplatebackendTransformDatasetRequest):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_transform_dataset(user, body)

    def dataset_service_revert_dataset(self, user, body:TemplatebackendRevertDatasetRequest):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_revert_dataset(user, body)

    def dataset_service_change_types_dataset(self, user, body:TemplatebackendChangeTypesDatasetRequest):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_change_types_dataset(user, body)
