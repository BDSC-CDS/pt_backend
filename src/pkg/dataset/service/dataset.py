from src.pkg.dataset.model.dataset import Dataset

class DatasetService:
    def __init__(self, dataset_store):
        self.dataset_store = dataset_store

    # store new dataset (store in metadata, dataset,values)
    def store_dataset(self, userid:int,tenantid:int, dataset_name:str,dataset: str,metadata_types=None):
        dataset_id = self.dataset_store.store_dataset(userid,tenantid,dataset_name,dataset)
        return dataset_id

    # get names of datasets related to this user (if not deleted)
    def get_list_datasets(self, userid:int, tenantid:int, offset:int,limit:int):
        datasets = self.dataset_store.get_list_datasets(userid=userid, tenantid=tenantid,offset=offset,limit=limit)
        return datasets

    # get metadata for a dataset (if not deleted)
    def get_dataset_metadata(self,name:str, userid:int, tenantid:int):
        dataset = self.dataset_store.get_dataset_metadata(name=name,userid=userid,tenantid=tenantid)
        return dataset

    # get dataset (if not deleted)
    def get_dataset_content(self,name:str, userid:int, tenantid:int, offset:int,limit:int):
        dataset = self.dataset_store.get_dataset_content(name=name,userid=userid,tenantid=tenantid, offset=offset,limit=limit)
        return dataset

    # delete dataset (just update deleted_at, don't actually delete it)
    def delete_dataset(self,name:str,userid:int, tenantid:int):
        deleted = self.dataset_store.delete_dataset(name=name,userid=userid,tenantid=tenantid)
        return deleted
