from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.dataset.model.dataset import Dataset,Metadata,Dataset_content
import csv
import pandas as pd

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

        try:
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
        except Exception as e:
                print(f"Error storing dataset: {e}")
                return None


    def get_list_datasets(self, userid:int, tenantid:int, offset:int,limit:int):
        query = "SELECT * FROM datasets WHERE userid = :userid AND tenantid = :tenantid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            try:
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
            except Exception as e:
                print(f"Error fetching datasets: {e}")
                return None

    def get_dataset_metadata(self,name:str, userid:int, tenantid:int):
        query1 = "SELECT * FROM datasets WHERE dataset_name=:name AND userid = :userid AND tenantid = :tenantid;"
        query2 = "SELECT * FROM metadata WHERE dataset_id = :dataset_id AND userid = :userid AND tenantid = :tenantid ORDER BY column_id;"
        with self.session_scope() as session:
            try:
                dataset = session.execute(text(query1), {
                    'name':name,
                    'userid': userid,
                    'tenantid': tenantid,
                }).mappings().fetchone()

                if dataset.deleted_at:
                    return # if the dataset was deleted we don't return anything (TODO)

                dataset_id = dataset.id
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
            except Exception as e:
                print(f"Error fetching metadata: {e}")
                return None



    def get_dataset_content(self,name:str, userid:int, tenantid:int, offset:int,limit:int): # TODO pagination
        # we order by column and line number
        query1 = "SELECT * FROM datasets WHERE dataset_name=:name AND userid = :userid AND tenantid = :tenantid;"
        query2 = "SELECT * FROM dataset_content WHERE dataset_id = :dataset_id AND userid = :userid AND tenantid = :tenantid ORDER BY column_id,line_id OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            try:
                dataset = session.execute(text(query1), {
                                'name':name,
                                'userid': userid,
                                'tenantid': tenantid,
                            }).mappings().fetchone()

                if not dataset or dataset.deleted_at:
                    print("Error: Dataset not found (might have been deleted).")
                    return None # if the dataset was deleted we don't return anything (TODO)

                dataset_id = dataset.id
                rows = session.execute(text(query2), {
                    'dataset_id': dataset_id,
                    'userid': userid,
                    'tenantid': tenantid,
                    'offset':offset,
                    'limit':limit
                }).mappings().fetchall() # get all values corresponding to dataset name and user id

                if not rows:
                    print("Error: No data found in the dataset.")
                    return None

                # Fetch the column names
                metadata_query = """
                    SELECT column_id, type_ FROM metadata WHERE dataset_id = :id AND userid = :userid AND tenantid = :tenantid ORDER BY column_id;
                """
                metadata = session.execute(text(metadata_query), {
                                                'dataset_id':dataset_id,
                                                'userid': userid,
                                                'tenantid': tenantid,
                                            }).mappings().fetchall()
                if not metadata:
                        print("Error: No metadata found for the dataset.")
                        return None
                # Create a dictionary to map column_id to column name
                column_names = {col_id: f"Column_{col_id}" for col_id, _ in metadata}

                # Create a dictionary to hold the data by columns
                data_dict = {column_names[col_id]: [] for col_id, _ in metadata}

                # Populate the data dictionary with values
                max_line = max(row[1] for row in rows)
                for col_id in column_names.keys():
                    data_dict[column_names[col_id]] = [''] * (max_line + 1)

                for col_id, line, value in rows:
                    data_dict[column_names[col_id]][line] = value
                # Create the DataFrame
                df = pd.DataFrame(data_dict)

                # result = [ Dataset_content(
                #         userid=val_.userid,
                #         tenantid=val_.tenantid,
                #         dataset_id=val_.dataset_id,
                #         column_id= val_.column_id,
                #         line_id= val_.line_id,
                #         val= val_.val,
                #     ) for val_ in rows ]

                return df

            except Exception as e:
                print(f"Error fetching dataset: {e}")
                return None



    def delete_dataset(self,name:str,userid:int, tenantid:int):
        query = """UPDATE datasets
                SET deleted_at = NOW()
                WHERE dataset_name = :name AND userid = :userid AND tenantid = :tenantid
                """
        with self.session_scope() as session:
            try:
                session.execute(text(query), {
                    'name': name,
                    'userid': userid,
                    'tenantid': tenantid,
                }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

                return True # TODO
            except Exception as e:
                print(f"Error deleting dataset: {e}")
                return None









    # def update_metadata_dataset(self,name:str,userid:int, tenantid:int,metadata:str):
    #     query = """UPDATE metadata
    #             SET col1 = :col1
    #             WHERE name = :name AND userid = :userid AND tenantid = :tenantid
    #             """ #TODO
    #     with self.session_scope() as session:
    #         session.execute(text(query), {
    #             'name': name,
    #             'userid': userid,
    #             'tenantid': tenantid,
    #         }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

    #         return True # TODO

    # # TODO qu'estce qu'on modifie
    # def update_dataset(self,name:str,userid:int, tenantid:int,dataset:Dataset):
    #     query = """UPDATE values
    #             SET col1 = :col1
    #             WHERE name = :name AND userid = :userid AND tenantid = :tenantid
    #             """ #TODO
    #     with self.session_scope() as session:
    #         session.execute(text(query), {
    #             'name': name,
    #             'userid': userid,
    #             'tenantid': tenantid,
    #         }) # TODO mappings ? fetchall? qu'est ce que ça retourne?

    #         return True # TODO
