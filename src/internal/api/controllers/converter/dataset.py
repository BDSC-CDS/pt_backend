from datetime import datetime
from typing import List

from src.pkg.dataset.model.dataset import Dataset, Metadata, Dataset_content
from server_template.models import TemplatebackendDataset
from server_template.models import TemplatebackendMetadata
from server_template.models import TemplatebackendColumn

# TODO
def dataset_to_business(dataset: TemplatebackendDataset) -> Dataset:
    d = Dataset(
        dataset_name = dataset.dataset_name,
    )
    return d

# TODO
def dataset_from_business(dataset: Dataset) -> TemplatebackendDataset:
    print(dataset)
    d = TemplatebackendDataset(
        id=dataset.id,
        dataset_name = dataset.dataset_name,
        created_at=dataset.created_at,
        deleted_at=dataset.deleted_at,
    )

    return d

def metadata_from_business(metadata: List[Metadata]) -> List[TemplatebackendMetadata]:
    print(metadata)
    m = [
        TemplatebackendMetadata(
            userid=met.userid,
            tenantid=met.tenantid,
            dataset_id=met.dataset_id,
            column_id=met.column_id,
            type=met.type_,
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
