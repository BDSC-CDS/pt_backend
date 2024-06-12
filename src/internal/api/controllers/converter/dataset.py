from datetime import datetime
from typing import List

from src.pkg.dataset.model.dataset import Dataset, Metadata, Dataset_content
from server_template.models import TemplatebackendDataset

# TODO add stuff
def dataset_to_business(dataset: TemplatebackendDataset) -> Dataset:
    d = Dataset(
        dataset_name = dataset.dataset_name,
    )
    return d

def dataset_from_business(dataset: Dataset) -> TemplatebackendDataset:
    print(dataset)
    d = TemplatebackendDataset(
        id=dataset.id,
        dataset_name = dataset.dataset_name,
        created_at=dataset.created_at,
        deleted_at=dataset.deleted_at,
    )

    return d
