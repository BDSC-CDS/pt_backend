from datetime import datetime
from io import StringIO
from typing import List
import pandas as pd

from src.pkg.dataset.model.dataset import Dataset, Metadata, Dataset_content
from server_template.models import TemplatebackendDataset
from server_template.models import TemplatebackendMetadata
from server_template.models import TemplatebackendColumn
from server_template.models import TemplatebackendStoreDatasetRequest
# TODO
def csv_to_business(user,body: TemplatebackendStoreDatasetRequest):
    name = body.dataset_name
    csv_data = StringIO(body.dataset)
    df = pd.read_csv(csv_data)
    dataset = Dataset(user.id, user.tenantid, name)

    dataset_entry = None
    metadatas = []
    contents = []

    # Example logic for populating data, adjust according to actual CSV structure
    for _, row in df.iterrows():
        # Create and append dataset object
        dataset = Dataset(userid=row['userid'], tenantid=row['tenantid'], dataset_name=body.dataset_name)
        datasets.append(dataset)

        # Assume multiple metadata entries per dataset
        metadata = Metadata(userid=row['userid'], tenantid=row['tenantid'], dataset_id=dataset.id, column_id=row['column_id'], type_=row['type'])
        metadatas.append(metadata)

        # Assume multiple content entries per dataset
        content = DatasetContent(userid=row['userid'], tenantid=row['tenantid'], dataset_id=dataset.id, column_id=row['column_id'], line_id=row['line_id'], val=row['val'])
        contents.append(content)

    return datasets, metadatas, contents

    return name,d

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
