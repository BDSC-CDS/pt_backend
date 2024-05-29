from src.pkg.dataset.model.dataset import Dataset

class DatasetService:
    def __init__(self, dataset_store):
        self.dataset_store = dataset_store

    # store new dataset (store in metadata, dataset,values)
    def store_dataset(self, dataset: Dataset): # TODO update csv?
        self.dataset_store.store_dataset(Dataset)

    # get names of datasets related to this user (if not deleted)
    def get_list_datasets(self, identifier:int, tenantid:int, offset:int,limit:int):
        datasets = self.dataset_store.get_list_datasets(identifier=identifier, tenantid=tenantid,offset=offset,limit=limit)
        return datasets

    # get metadata for a dataset (if not deleted)
    def get_dataset_metadata(self,name:str, identifier:int, tenantid:int):
        dataset = self.dataset_store.get_dataset_metadata(name=name,identifier=identifier,tenantid=tenantid)
        return dataset

    # get dataset (if not deleted)
    def get_dataset(self,name:str, identifier:int, tenantid:int, offset:int,limit:int):
        dataset = self.dataset_store.get_dataset(name=name,identifier=identifier,tenantid=tenantid, offset=offset,limit=limit)
        return dataset

    # TODO how would we modify the metadata
    def update_metadata_dataset(self,name:str,identifier:int, tenantid:int,metadata:str):
        updated = self.dataset_store.update_metadata_dataset(name=name, identifier=identifier, tenantid=tenantid,metadata=metadata)
        return updated

    # TODO just replace dataset?
    def update_dataset(self,name:str,identifier:int, tenantid:int,dataset: Dataset):
        updated = self.dataset_store.update_dataset(name=name, identifier=identifier, tenantid=tenantid,dataset=dataset)
        return updated

    # delete dataset (just update deleted_at, don't actually delete it)
    def delete_dataset(self,name:str,identifier:int, tenantid:int):
        deleted = self.dataset_store.delete_dataset(name=name,identifier=identifier,tenantid=tenantid)
        return deleted
