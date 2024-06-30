import traceback
from typing import List

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
from server_template.models import TemplatebackendTransformDatasetResult
from server_template.models import TemplatebackendTransformDatasetReply
from server_template.models import TemplatebackendTransformDatasetRequest

import src.internal.api.controllers.converter.dataset as dataset_converter

class DatasetController:
    def __init__(self, dataset_service):
        self.dataset_service = dataset_service

    def dataset_service_store_dataset(self, user, body: TemplatebackendStoreDatasetRequest):
        # name, csv = dataset_converter.csv_to_business(body)
        try:
            # TODO metadata types
            dataset_id = self.dataset_service.store_dataset(user.id,user.tenantid, body.dataset_name, body.dataset, body.types)
            print("Dataset controller Id", dataset_id)
            return TemplatebackendStoreDatasetReply(TemplatebackendStoreDatasetResult(id=dataset_id))

        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

    def dataset_service_delete_dataset(self, user, id:int ):
        try:
            result = self.dataset_service.delete_dataset(id, user.id, user.tenantid)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        return TemplatebackendDeleteDatasetReply(TemplatebackendDeleteDatasetResult(success=result))

    def dataset_service_get_dataset_metadata(self, user, id: int):
        try:
            metadata = self.dataset_service.get_dataset_metadata(id,user.id,user.tenantid)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if metadata is None:
            return TemplatebackendGetDatasetMetadataReply(TemplatebackendGetDatasetMetadataResult(metadata=None)), 404
        metadata = dataset_converter.metadata_from_business(metadata)
        return TemplatebackendGetDatasetMetadataReply(TemplatebackendGetDatasetMetadataResult(metadata=metadata))

    def dataset_service_get_dataset_content(self, user, id: int,offset: int=None, limit: int=None):
        try:
            dataset_content = self.dataset_service.get_dataset_content(id,user.id,user.tenantid,offset,limit)
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


    def dataset_service_transform_dataset(self, user, body:TemplatebackendTransformDatasetRequest):
        try:
            new_dataset : List[List[str]] = self.dataset_service.transform_dataset(user.id,user.tenantid,body.dataset_id,body.config_id)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        return TemplatebackendTransformDatasetReply(TemplatebackendTransformDatasetResult(columns=new_dataset))
