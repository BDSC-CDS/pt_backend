from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.dataset.model.dataset import Dataset
import csv


def infer_column_type(values):
    is_int = True
    is_float = True

    for value in values:
        try:
            int(value)
        except ValueError:
            is_int = False

        try:
            float(value)
        except ValueError:
            is_float = False

    if is_int:
        return "INTEGER"
    elif is_float:
        return "FLOAT"
    else:
        return "TEXT"


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

    def store_dataset(self, user_id:int,tenant_id:int, dataset_name:str,path: str,metadata_types=None):
        # Insert dataset entry and get the generated dataset_id
        dataset_query = """
            INSERT INTO datasets
                (userid, tenantid, dataset_name,created_at)
            VALUES
                 (:userid, :tenantid, :dataset_name, NOW())
            RETURNING id;
        """
        dataset_id = 0
        with self.session_scope() as session:
            try:
                result = session.execute(text(dataset_query), {
                    'userid': user_id,
                    'tenantid': tenant_id,
                    'name':dataset_name,
                }).fetchone()
                dataset_id = result[0]

            except SQLAlchemyError as e:
                raise e


        # Read the CSV file once to infer column types
        with open(path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)  # Read the header row
            column_data = [[] for _ in headers]
            for row in csv_reader:
                for col_index, value in enumerate(row):
                    column_data[col_index].append(value)

                # Infer types for each column
            column_types = {}
            for col_index, header in enumerate(headers):
                if metadata_types and header in metadata_types:
                    column_types[header] = metadata_types[header]
                else:
                    column_types[header] = infer_column_type(column_data[col_index])

            # Insert metadata
            metadata_to_insert = []
            for column_id, header in enumerate(headers):
                column_type = column_types[header]
                metadata_to_insert.append((user_id, tenant_id, dataset_id, column_id, column_type))
            query = """
                INSERT INTO metadata (user_id, tenant_id, dataset_id, column_id, type)
                VALUES (%s, %s, %s, %s, %s);
            """
            with self.session_scope() as session:
                try:
                    session.execute(query,metadata_to_insert) # TODO verifier que ça fonctionne
                except SQLAlchemyError as e:
                    raise e

        # insert data content



####### old ##########################
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
