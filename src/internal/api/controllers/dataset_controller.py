import traceback
from typing import List
import io
import flask

from server_template.models import TemplatebackendStoreDatasetReply
from server_template.models import TemplatebackendStoreDatasetResult
from server_template.models import TemplatebackendStoreDatasetRequest
from server_template.models import TemplatebackendGetDatasetInfoReply
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
from server_template.models import TemplatebackendRevertDatasetReply
from server_template.models import TemplatebackendRevertDatasetRequest
from server_template.models import TemplatebackendChangeTypesDatasetRequest
from server_template.models import TemplatebackendChangeTypesDatasetReply
from server_template.models import TemplatebackendGetDatasetJupyterhubReply
from server_template.models import TemplatebackendGetDatasetJupyterhubResult
from server_template.models import ApiHttpBody

import src.internal.api.controllers.converter.dataset as dataset_converter

class DatasetServiceController:
    def __init__(self, dataset_service):
        self.dataset_service = dataset_service

    def dataset_service_store_dataset(self, user, body: TemplatebackendStoreDatasetRequest):
        # name, csv = dataset_converter.csv_to_business(body)
        try:
            dataset_id = self.dataset_service.store_dataset(user.id,user.tenantid, body.dataset_name, body.dataset, body.types, body.identifiers, body.is_id)
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

    def dataset_service_get_dataset_info(self, user, id: int):
        try:
            dataset = self.dataset_service.get_dataset_info(id,user.id,user.tenantid)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if dataset is None:
            return TemplatebackendGetDatasetInfoReply(dataset=None), 404
        dataset = dataset_converter.dataset_from_business(dataset)
        return TemplatebackendGetDatasetInfoReply(dataset=dataset)

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
            dataset_content, n_rows = self.dataset_service.get_dataset_content(id,user.id,user.tenantid,offset,limit)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        if dataset_content is None:
            return TemplatebackendGetDatasetContentReply(TemplatebackendGetDatasetContentResult(columns=None, n_rows=0))
        dataset_content = dataset_converter.content_from_business(dataset_content)
        return TemplatebackendGetDatasetContentReply(TemplatebackendGetDatasetContentResult(columns=dataset_content, n_rows=n_rows))
    
    def dataset_service_get_dataset_csv(self, user, id: int, offset: int=None, limit: int=None):
        try:
            df = self.dataset_service.get_dataset_as_dataframe(id,user.id,user.tenantid)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        
        if df is None:
            return None, 404
        
        buffer = io.BytesIO()
        df.to_csv(buffer, index=False, lineterminator='\n')
        bytes = buffer.getvalue()

        headers = {
            "Content-Type": "text/csv",
        }

        resp = flask.Response(bytes, headers=headers)

        return resp, 200, headers

    def dataset_service_get_dataset_dataframe(self, user, id: int, offset: int=None, limit: int=None):
        try:
            df = self.dataset_service.get_dataset_as_dataframe(id,user.id,user.tenantid)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

        if df is None:
            return None, 404

        buffer = io.BytesIO()
        df.to_parquet(buffer)
        bytes = buffer.getvalue()

        headers = {
            "Content-Type": "application/vnd.apache.parquet",
        }

        resp = flask.Response(bytes, headers=headers)
        
        return resp, 200, headers

    def dataset_service_get_dataset_jupyterhub(self, user, id: int):
        url = self.dataset_service.open_jupyterhub_deidentification(user.id, id)

        return TemplatebackendGetDatasetJupyterhubReply(TemplatebackendGetDatasetJupyterhubResult(url=url))



    def dataset_service_get_dataset_identifier(self, user, id: int,offset: int=None, limit: int=None):
        try:
            dataset_content, n_rows = self.dataset_service.get_identifiers_and_quasi_dataset(id,user.id,user.tenantid,offset,limit)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        if dataset_content is None:
            return TemplatebackendGetDatasetContentReply(TemplatebackendGetDatasetContentResult(columns=None, n_rows=0))
        dataset_content = dataset_converter.content_from_business(dataset_content)
        return TemplatebackendGetDatasetContentReply(TemplatebackendGetDatasetContentResult(columns=dataset_content, n_rows=n_rows))

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
            new_dataset_id = self.dataset_service.transform_dataset(user.id,user.tenantid,body.dataset_id,body.config_id)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        return TemplatebackendTransformDatasetReply(TemplatebackendTransformDatasetResult(id=new_dataset_id))

    def dataset_service_revert_dataset(self, user, body:TemplatebackendRevertDatasetRequest):
        try:
            new_dataset_id = self.dataset_service.revert_dataset(user.id,user.tenantid,body.id)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        return TemplatebackendRevertDatasetReply(id=new_dataset_id)

    def dataset_service_change_types_dataset(self, user, body:TemplatebackendChangeTypesDatasetRequest):
        try:
            metadata = dataset_converter.metadata_to_business(body.metadata)
            new_dataset_id = self.dataset_service.change_types_dataset(user.id,user.tenantid,body.dataset_id, metadata)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        return TemplatebackendChangeTypesDatasetReply(id=new_dataset_id)
