from datetime import datetime
from io import StringIO
from typing import List
# import pandas as pd

from src.pkg.dataset.model.dataset import Dataset, Metadata, Dataset_content
from server_template.models import TemplatebackendDataset
from server_template.models import TemplatebackendMetadata
from server_template.models import TemplatebackendColumn
from server_template.models import TemplatebackendStoreDatasetRequest

def dataset_from_business(dataset: Dataset) -> TemplatebackendDataset:
    print(dataset)
    d = TemplatebackendDataset(
        id=dataset.id,
        dataset_name = dataset.dataset_name,
        created_at=dataset.created_at,
        deleted_at=dataset.deleted_at,
    )

    return d

def metadata_to_business(metadata: List[TemplatebackendMetadata] ) -> List[Metadata]:
    m = [
        Metadata(
            userid=met.userid,
            tenantid=met.tenantid,
            dataset_id=met.dataset_id,
            column_id=met.column_id,
            column_name=met.column_name,
            type_=met.type,
            identifier=met.identifier,
            is_id=met.is_id,
        ) for met in metadata
    ]
    return m

def metadata_from_business(metadata: List[Metadata]) -> List[TemplatebackendMetadata]:
    print(metadata)
    m = [
        TemplatebackendMetadata(
            userid=met.userid,
            tenantid=met.tenantid,
            dataset_id=met.dataset_id,
            column_id=met.column_id,
            column_name=met.column_name,
            type=met.type_,
            identifier=met.identifier,
            is_id=met.is_id,
        ) for met in metadata
    ]
    return m

def datasets_from_business(datasets: List[Dataset]) -> List[TemplatebackendDataset]:
    print(datasets)
    d = [
        TemplatebackendDataset(
            id=data.id,
            userid=data.userid,
            tenantid=data.tenantid,
            dataset_name=data.dataset_name,
            created_at=data.created_at,
            deleted_at=data.deleted_at
        ) for data in datasets
    ]
    return d

def content_from_business(columns: List[List[str]]) -> List[TemplatebackendColumn]:
    print(columns)
    c = [
        TemplatebackendColumn(
            value=col
        ) for col in columns
    ]
    return c
