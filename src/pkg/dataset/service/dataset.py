from src.pkg.dataset.model.dataset import Dataset

class DatasetService:
    def __init__(self, dataset_store):
        self.dataset_store = dataset_store

    def store_dataset(self, dataset: Dataset):
        self.dataset_store.store_dataset(Dataset)

    def get_datasets(self,offset:int,limit:int):
        datasets = self.dataset_store.get_dataset(offset,limit)
        return datasets

    def get_datasets_for_user(self, identifier:int,offset:int,limit:int):
        datasets = self.dataset_store.get_datasets_for_user(identifier=identifier,offset=offset,limit=limit)
        return datasets

    def get_dataset_by_name(self,name:str):
        dataset = self.dataset_store.get_dataset_by_name(name=name)
        return dataset
