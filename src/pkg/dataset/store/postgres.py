from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.dataset.model.dataset import Dataset,Metadata,Dataset_content
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

    def store_dataset(self, userid:int,tenantid:int, dataset_name:str,path: str,metadata_types=None):
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
                    'userid': userid,
                    'tenantid': tenantid,
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
                metadata_to_insert.append((userid, tenantid, dataset_id, column_id, column_type))
            query = """
                INSERT INTO metadata (userid, tenantid, dataset_id, column_id, type_)
                VALUES (%s, %s, %s, %s, %s);
            """
            with self.session_scope() as session:
                try:
                    session.execute(query,metadata_to_insert) # TODO verifier que ça fonctionne
                except SQLAlchemyError as e:
                    raise e

            # insert data content
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            data_to_insert = []
            for line_number, row in enumerate(csv_reader):
                for column_id, value in enumerate(row):
                    data_to_insert.append((userid, tenantid, dataset_id, column_id, line_number, value))

                    # Batch insert every 1000 rows
                    if len(data_to_insert) >= 1000:
                        query = """
                            INSERT INTO dataset_content (userid, tenantid, dataset_id, column_id, line_id, val)
                            VALUES (%s, %s, %s, %s, %s, %s);
                        """
                        with self.session_scope() as session:
                            try:
                                session.execute(query,data_to_insert) # TODO verifier que ça fonctionne
                            except SQLAlchemyError as e:
                                raise e
                        data_to_insert = []

            if data_to_insert:
                query = """
                            INSERT INTO dataset_content (userid, tenantid, dataset_id, column_id, line_id, val)
                            VALUES (%s, %s, %s, %s, %s, %s);
                        """
                with self.session_scope() as session:
                    try:
                        session.execute(query,data_to_insert) # TODO verifier que ça fonctionne
                    except SQLAlchemyError as e:
                        raise e

            return dataset_id


    def get_list_datasets(self, userid:int, tenantid:int, offset:int,limit:int):
        query = "SELECT * FROM datasets WHERE userid = :userid AND tenantid = :tenantid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            datasets = session.execute(text(query), {
                'userid': userid,
                'tenantid': tenantid,
                'offset':offset,
                'limit':limit
            }).mappings().fetchall()

            result = [
                Dataset(
                    userid=dataset.userid,
                    tenantid=dataset.tenantid,
                    dataset_name=dataset.dataset_name,
                    id=dataset.id,
                    created_at= dataset.created_at,
                    deleted_at= dataset.deleted_at,
                ) for dataset in datasets if dataset.deleted_at is None # we only take the datasets that have not been deleted
            ]

            return result

    def get_dataset_metadata(self,dataset_id:int, userid:int, tenantid:int):
        query1 = "SELECT * FROM datasets WHERE id=:id AND userid = :userid AND tenantid = :tenantid;"
        query2 = "SELECT * FROM metadata WHERE dataset_id = :dataset_id AND userid = :userid AND tenantid = :tenantid ORDER BY column_id;"
        with self.session_scope() as session:
            dataset = session.execute(text(query1), {
                'id':dataset_id,
                'userid': userid,
                'tenantid': tenantid,
            }).mappings().fetchone()

            if dataset.deleted_at:
                return # if the dataset was deleted we don't return anything (TODO)

            metadatas = session.execute(text(query2), {
                'dataset_id':dataset_id,
                'userid': userid,
                'tenantid': tenantid,
            }).mappings().fetchall()

            result = [
                Metadata(
                    userid=metadata.userid,
                    tenantid=metadata.tenantid,
                    dataset_id=metadata.dataset_id,
                    column_id= metadata.column_id,
                    type_= metadata.type_
                ) for metadata in metadatas ]

            return result



    def get_dataset(self, name:str,userid:int, tenantid:int, offset:int, limit:int):
        # TODO order by line number?
        query = "SELECT * FROM values WHERE name = :name AND userid = :userid AND tenantid = :tenantid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            values = session.execute(text(query), {
                'name': name,
                'userid': userid,
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


    def update_metadata_dataset(self,name:str,userid:int, tenantid:int,metadata:str):
        query = """UPDATE metadata
                SET col1 = :col1
                WHERE name = :name AND userid = :userid AND tenantid = :tenantid
                """ #TODO
        with self.session_scope() as session:
            session.execute(text(query), {
                'name': name,
                'userid': userid,
                'tenantid': tenantid,
            }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

            return True # TODO

    # TODO qu'estce qu'on modifie
    def update_dataset(self,name:str,userid:int, tenantid:int,dataset:Dataset):
        query = """UPDATE values
                SET col1 = :col1
                WHERE name = :name AND userid = :userid AND tenantid = :tenantid
                """ #TODO
        with self.session_scope() as session:
            session.execute(text(query), {
                'name': name,
                'userid': userid,
                'tenantid': tenantid,
            }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

            return True # TODO

    def delete_dataset(self,name:str,userid:int, tenantid:int):
        query = """UPDATE dataset
                SET deletedat = NOW()
                WHERE name = :name AND userid = :userid AND tenantid = :tenantid
                """ #TODO
        with self.session_scope() as session:
            session.execute(text(query), {
                'name': name,
                'userid': userid,
                'tenantid': tenantid,
            }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

            return True # TODO
