import traceback

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

import src.internal.api.controllers.converter.dataset as dataset_converter
from src.pkg.dataset.service.dataset import DatasetService

# TODO implement logic
class DatasetController:
    def __init__(self, dataset_service):
        self.dataset_service = dataset_service

    def dataset_service_store_dataset(self, user, body: TemplatebackendStoreDatasetRequest):
        # name, csv = dataset_converter.csv_to_business(body)
        try:
            # TODO where do I find tenantid?
            # TODO metadata types
            dataset = self.dataset_service.store_dataset(user.id,user.tenantid, body.dataset_name, body.dataset)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        # return new dataset id
        return TemplatebackendStoreDatasetReply(TemplatebackendStoreDatasetResult(id=dataset.id))

    def dataset_service_delete_dataset(self, user, name:str ):
        try:
            #TODO tenantid
            result = self.dataset_service.delete_dataset(name, user.id, user.tenantid)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        return TemplatebackendDeleteDatasetReply(TemplatebackendDeleteDatasetResult(success=result))

    def dataset_service_get_dataset_metadata(self, user, name: str):
        try:
            metadata = self.dataset_service.get_dataset_metadata(name,user.id,user.tenantid)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if metadata is None:
            return TemplatebackendGetDatasetMetadataReply(TemplatebackendGetDatasetMetadataResult(metadata=None)), 404
        metadata = dataset_converter.metadata_from_business(metadata)
        return TemplatebackendGetDatasetMetadataReply(TemplatebackendGetDatasetMetadataResult(metadata=metadata))

    def dataset_service_get_dataset_content(self, user, name: str,offset: int=None, limit: int=None):
        try:
            dataset_content = self.dataset_service.get_dataset_content(name,user.id,user.tenantid,offset,limit)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        if dataset_content is None:
            return TemplatebackendGetDatasetContentReply(TemplatebackendGetDatasetContentResult(columns=None))
        dataset_content = dataset_converter.content_from_business(dataset_content)
        return TemplatebackendGetDatasetContentReply(TemplatebackendGetDatasetContentResult(columns=dataset_content))

    def dataset_service_list_datasets(self, user, offset: int=None, limit: int=None):
        try:
            datasets = self.dataset_service.get_list_datasets(user.id,user.tenantid,offset,limit)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if datasets is None:
            return TemplatebackendListDatasetsReply(TemplatebackendListDatasetsResult(datasets==None)), 404

        datasets = dataset_converter.datasets_from_business(datasets)

        return TemplatebackendListDatasetsReply(TemplatebackendListDatasetsResult(datasets=datasets))
