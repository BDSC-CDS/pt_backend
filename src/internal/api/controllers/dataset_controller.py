from server_template.models import TemplatebackendStoreDatasetReply
from server_template.models import TemplatebackendStoreDatasetResult
from server_template.models import TemplatebackendStoreDatasetRequest
from server_template.models import TemplatebackendGetDatasetMetadataReply
from server_template.models import TemplatebackendGetDatasetMetadataResult
from server_template.models import TemplatebackendListDatasetsReply
from server_template.models import TemplatebackendListDatasetsResult
from server_template.models import TemplatebackendGetDatasetContentReply
from server_template.models import TemplatebackendGetDatasetContentResult
from server_template.models import TemplatebackendDeleteDatasetReply
from server_template.models import TemplatebackendDeleteDatasetResult

# TODO implement logic
class DatasetController:
    def __init__(self, config, dataset_service):
        self.config = config
        self.authentication_service = dataset_service

    def dataset_service_store_dataset(self, user, body: TemplatebackendStoreDatasetRequest):
        return TemplatebackendStoreDatasetReply(TemplatebackendStoreDatasetResult())

    def dataset_service_delete_dataset(self, user, name: str):
        return TemplatebackendDeleteDatasetReply(TemplatebackendDeleteDatasetResult())

    def dataset_service_get_dataset_metadata(self, user, name: str):
        return TemplatebackendGetDatasetMetadataReply(TemplatebackendGetDatasetMetadataResult())

    def dataset_service_get_dataset_content(self, user, name: str,offset: int=None, limit: int=None):
        return TemplatebackendGetDatasetContentReply(TemplatebackendGetDatasetContentResult())

    def dataset_service_list_datasets(self, user, offset: int=None, limit: int=None):
        return TemplatebackendListDatasetsReply(TemplatebackendListDatasetsResult())
