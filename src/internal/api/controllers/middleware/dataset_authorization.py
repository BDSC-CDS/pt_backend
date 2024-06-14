from server_template.models import TemplatebackendDataset
from server_template.models import TemplatebackendStoreDatasetRequest

# from server_template.models import TemplatebackendUpdatePasswordRequest
from src.internal.api.controllers.dataset_controller import DatasetController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class DatasetControllerAuthentication():
    def __init__(self, next: DatasetController):
        self.next = next
        implements_interface(DatasetController, DatasetControllerAuthentication)

    def dataset_service_store_dataset(self, user, body: TemplatebackendStoreDatasetRequest):
        if not is_authenticated(user): # TODO is_self ? comment on vérifie que qu'il accède a son propre dataset ?
            return None, 403
        return self.next.dataset_service_store_dataset(user, body)

    def dataset_service_delete_dataset(self, user,name:str):
        # if not is_admin_or_self(user, id):
        #     return None, 403
        # TODO remettre ?
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_delete_dataset(user,id, name)

    def dataset_service_get_dataset_metadata(self, user, name: str):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_metadata(user, name)

    def dataset_service_get_dataset_content(self, user, name: str,offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_get_dataset_content(user, name,offset,limit)

    def dataset_service_list_datasets(self, user, offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        return self.next.dataset_service_list_datasets(user, offset,limit)
