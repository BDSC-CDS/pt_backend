import io
import os
import uuid
from typing import List
from jinja2 import Template
from src.pkg.dataset.model.dataset import Dataset, Metadata
import pandas as pd
import jupytext

class DatasetService:
    def __init__(self, config, dataset_store, authentication_service, jupyterhub_client):
        self.config = config
        self.dataset_store = dataset_store
        self.authentication_service = authentication_service
        self.jupyterhub_client = jupyterhub_client
        
        with open(os.path.join(os.path.dirname(__file__), "notebook_template.py"), "r") as f:
            self.template = f.read()

    # store new dataset (store in metadata, dataset,values)
    def store_dataset(self, userid:int,tenantid:int, dataset_name:str,dataset: str,types:str, identifiers:str, is_id:str):
        dataset_id = self.dataset_store.store_dataset(userid,tenantid,dataset_name,dataset,types,identifiers, is_id)
        return dataset_id

    # get names of datasets related to this user (if not deleted)
    def get_list_datasets(self, userid:int, tenantid:int, offset:int,limit:int):
        datasets = self.dataset_store.get_list_datasets(userid=userid, tenantid=tenantid,offset=offset,limit=limit)
        return datasets

    # get the info of a dataset
    def get_dataset_info(self,id:int, userid:int, tenantid:int):
        dataset = self.dataset_store.get_dataset_info(id=id,userid=userid,tenantid=tenantid)
        return dataset

    # get metadata for a dataset (if not deleted)
    def get_dataset_metadata(self,id:int, userid:int, tenantid:int):
        dataset = self.dataset_store.get_dataset_metadata(id=id,userid=userid,tenantid=tenantid)
        return dataset

    # get dataset (if not deleted)
    def get_dataset_content(self,id:int, userid:int, tenantid:int, offset:int,limit:int):
        dataset,n_rows = self.dataset_store.get_dataset_content(id=id,userid=userid,tenantid=tenantid, offset=offset,limit=limit)
        return dataset, n_rows

    def get_dataset_as_dataframe(store, dataset_id: int, userid: int, tenantid: int) -> pd.DataFrame:
        content, n_rows = store.get_dataset_content(dataset_id, userid, tenantid, 0, None)
        metadata = store.get_dataset_metadata(dataset_id, userid, tenantid)

        # Create column names from metadata
        column_names = [meta.column_name for meta in metadata]

        # Transpose content to match the columnar structure
        transposed_content = list(zip(*content))

        # Create the DataFrame
        df = pd.DataFrame(transposed_content, columns=column_names)

        # Enforce data types from metadata
        type_mapping = {"string": str, "int": int, "float": float, "bool": bool}
        for meta in metadata:
            if meta.type_ in type_mapping:
                # TODO centralize and improve type serialization
                try:
                    df[meta.column_name] = df[meta.column_name].astype(type_mapping[meta.type_])
                except Exception as e:
                    print("Error swapping type " + meta.type_ + " for column " + meta.column_name + " of dataset " + dataset_id, e)
        return df

    def open_jupyterhub_deidentification(self, userid: int, datasetid: int):
    
        token = self.authentication_service.userid_to_token(userid)
        user = self.authentication_service.token_to_user(token)
    
        template = Template(self.template)
        context = {
            "datasetid": datasetid,
            "token": token,
            "username": user.username,
            "backend_public_url": self.config.daemon.public_url,
            "arx_service_url": self.config.clients.arx.host,
        }
        text = template.render(context)

        # text to buffer
        fp = io.StringIO(text)
        notebook = jupytext.read(fp, fmt = "py:percent")

        buffer = io.StringIO()
        jupytext.write(notebook, buffer, fmt="ipynb")
        notebook_bytes = buffer.getvalue().encode("utf-8")

        self.jupyterhub_client.create_user(user.username)
        namedserver_uuid = str(uuid.uuid4())
        self.jupyterhub_client.launch_named_server(user.username, namedserver_uuid)

        if self.config.clients.jupyterhub.debug: 
            with open(os.path.join(os.path.dirname(__file__), "debug_notebook.ipynb"), "wb") as f:
                f.write(notebook_bytes)
        
        url = self.jupyterhub_client.get_authenticate_user_url(user.username, token, notebook_bytes, namedserver_uuid)
        return url

    # get only identifying and quasi-identifying columns of dataset
    def get_identifiers_and_quasi_dataset(self,id:int, userid:int, tenantid:int, offset:int,limit:int):
        dataset,n_rows = self.dataset_store.get_identifiers_and_quasi_dataset(id=id,userid=userid,tenantid=tenantid, offset=offset,limit=limit)
        return dataset, n_rows

    # delete dataset (just update deleted_at, don't actually delete it)
    def delete_dataset(self,id:int,userid:int, tenantid:int):
        deleted = self.dataset_store.delete_dataset(id=id,userid=userid,tenantid=tenantid)
        return deleted

    # transform a dataset based on a configuration
    def transform_dataset(self,userid:int,tenantid:int,dataset_id:int,config_id:int):
        new_dataset = self.dataset_store.transform_dataset(userid,tenantid,dataset_id,config_id)
        return new_dataset

    # revert a dataset to its state before transforming
    def revert_dataset(self,userid:int,tenantid:int,dataset_id:int):
        new_dataset = self.dataset_store.revert_dataset(userid,tenantid,dataset_id)
        return new_dataset

    # change the types of dataset to a new dataset
    def change_types_dataset(self,userid:int, tenantid:int,dataset_id:int,new_metadata: List[Metadata]):
        new_dataset = self.dataset_store.change_types_dataset(userid,tenantid, dataset_id, new_metadata)
        return new_dataset
