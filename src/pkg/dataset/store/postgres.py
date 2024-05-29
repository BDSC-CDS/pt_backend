from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.dataset.model.dataset import Dataset

class DatasetStore:
    def __init__(self, db: Engine):
        self.db = db

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        Session = sessionmaker(bind=self.db)
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def store_dataset(self, dataset: Dataset):
        dataset_query = """
INSERT INTO datasets
    (userid, name, data, created_at, updated_at)
VALUES
    (:userid, :name, :data, NOW(), NOW())
RETURNING id;
"""
        with self.session_scope() as session:
            try:
                result = session.execute(text(dataset_query), {
                    'userid': dataset.userid,
                    'name':dataset.name,
                    'data': dataset.data,
                }).fetchone()
                dataset_id = result[0]

            except SQLAlchemyError as e:
                raise e

            return Dataset(id=dataset_id)

    def get_list_datasets(self, identifier:int, tenantid:int, offset:int,limit:int):
        query = "SELECT * FROM datasets WHERE userid = :userid AND tenantid = :tenantid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            datasets = session.execute(text(query), {
                'userid': identifier,
                'tenantid': tenantid,
                'offset':offset,
                'limit':limit
            }).mappings().fetchall()

            result = [
               Dataset( # TODO what is in the dataset (name,user)
                    id=dataset.id,
                    userid=dataset.userid,
                    name=dataset.name,
                    # data=dataset.data,
                    created_at= dataset.created_at
                ) for dataset in datasets
            ]
            return result

    def get_dataset_metadata(self,name:str, identifier:int, tenantid:int):
        query = "SELECT * FROM dataset_metadata WHERE name = :name AND userid = :userid AND tenantid = :tenantid;"
        with self.session_scope() as session:
            metadata = session.execute(text(query), {
                'name':name,
                'userid': identifier,
                'tenantid': tenantid,
            }).mappings().fetchone() # fetch first

            result = Metadata( # TODO what is in the metadata (name,user)
                    id=metadata.id,
                    userid=metadata.userid,
                    name=metadata.name,
                    # data=dataset.data,
                    created_at= metadata.created_at
                )

            return result



    def get_dataset(self, name:str,identifier:int, tenantid:int, offset:int, limit:int):
        # TODO order by line number?
        query = "SELECT * FROM values WHERE name = :name AND userid = :userid AND tenantid = :tenantid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            values = session.execute(text(query), {
                'name': name,
                'userid': identifier,
                'tenantid': tenantid,
                'offset':offset,
                'limit':limit
            }).mappings().fetchall() # get all values corresponding to dataset name and user id

            result = [ Value( # TODO
                    id=val.id,
                    userid=val.userid,
                    name=val.name,
                    data=val.data,
                    created_at= val.created_at
                ) for val in values ]

            return result


    def update_metadata_dataset(self,name:str,identifier:int, tenantid:int,metadata:str):
        query = """UPDATE metadata
                SET col1 = :col1
                WHERE name = :name AND userid = :userid AND tenantid = :tenantid
                """ #TODO
        with self.session_scope() as session:
            session.execute(text(query), {
                'name': name,
                'userid': identifier,
                'tenantid': tenantid,
            }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

            return True # TODO

    # TODO qu'estce qu'on modifie
    def update_dataset(self,name:str,identifier:int, tenantid:int,dataset:Dataset):
        query = """UPDATE values
                SET col1 = :col1
                WHERE name = :name AND userid = :userid AND tenantid = :tenantid
                """ #TODO
        with self.session_scope() as session:
            session.execute(text(query), {
                'name': name,
                'userid': identifier,
                'tenantid': tenantid,
            }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

            return True # TODO

    def delete_dataset(self,name:str,identifier:int, tenantid:int):
        query = """UPDATE dataset
                SET deletedat = NOW()
                WHERE name = :name AND userid = :userid AND tenantid = :tenantid
                """ #TODO
        with self.session_scope() as session:
            session.execute(text(query), {
                'name': name,
                'userid': identifier,
                'tenantid': tenantid,
            }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

            return True # TODO
