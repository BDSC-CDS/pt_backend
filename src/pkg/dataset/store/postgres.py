from io import StringIO
from typing import List
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.dataset.model.dataset import Dataset,Metadata,Dataset_content
import csv
from collections import defaultdict
import json
import random
from datetime import datetime, timedelta
from dateutil import parser

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

    def store_dataset(self, userid:int,tenantid:int, dataset_name:str,dataset: str,types:str) -> int:
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
                    'dataset_name':dataset_name,
                }).fetchone()
                dataset_id = result[0]

            except SQLAlchemyError as e:
                raise e

        try:
                csv_data = dataset.replace("\\n", "\n")
                csvfile = StringIO(csv_data)

                # Read the CSV file once to infer column type
                # with open(path, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                headers = next(csv_reader)  # Read the header row

                column_data = [[] for _ in headers]
                for row in csv_reader:
                    for col_index, value in enumerate(row):
                        column_data[col_index].append(value)

                # Infer types for each column
                # column_types = {}
                # for col_index, header in enumerate(headers):
                #     if metadata_types and header in metadata_types:
                #         column_types[header] = metadata_types[header]
                #     else:
                #         column_types[header] = infer_column_type(column_data[col_index])
                # Insert metadata
                print("TYPES: ",types)
                column_types = json.loads(types)
                print("JSON TYPES: ", column_types)

                metadata_to_insert = []
                for column_id, header in enumerate(headers):
                    column_type = column_types[header]
                    column_name = header
                    metadata_to_insert.append((int(userid), int(tenantid), int(dataset_id), int(column_id), str(column_name), str(column_type)))
                query = """
                    INSERT INTO metadata (userid, tenantid, dataset_id, column_id, column_name, type_)
                    VALUES (:userid, :tenantid, :dataset_id, :column_id, :column_name, :type_);
                """
                with self.session_scope() as session:
                    try:
                        #session.execute(text(query),metadata_to_insert) # TODO verifier que ça fonctionne
                        for record in metadata_to_insert:
                            session.execute(text(query), {
                                'userid': record[0],
                                'tenantid': record[1],
                                'dataset_id': record[2],
                                'column_id': record[3],
                                'column_name': record[4],
                                'type_': record[5]
                            })
                    except SQLAlchemyError as e:
                        raise e

                # # insert data content
                csvfile.seek(0)
                csv_reader = csv.reader(csvfile)
                print("csv reader")
                next(csv_reader)  # Skip the header row
                print("skipped header")
                data_to_insert = []
                print("before loop")
                for line_number, row in enumerate(csv_reader):
                    print("line number: ", line_number)
                    for column_id, value in enumerate(row):
                        #data_to_insert.append((userid, tenantid, dataset_id, column_id, line_number, value))

                        # Batch insert every 1000 rows TODO
                        #if len(data_to_insert) >= 1000:
                        query = """
                            INSERT INTO dataset_content (userid, tenantid, dataset_id, column_id, line_id, val)
                            VALUES (:userid, :tenantid, :dataset_id, :column_id, :line_id, :val);
                        """
                        with self.session_scope() as session:
                            try:
                                # session.execute(text(query),data_to_insert)
                                # for record in data_to_insert:
                                    session.execute(text(query), {
                                        'userid': userid,
                                        'tenantid': tenantid,
                                        'dataset_id': dataset_id,
                                        'column_id': column_id,
                                        'line_id': line_number,
                                        'val': value
                                    })
                            except SQLAlchemyError as e:
                                raise e
                            #data_to_insert = []

                # if data_to_insert:
                #     query = """
                #                 INSERT INTO dataset_content (userid, tenantid, dataset_id, column_id, line_id, val)
                #                 VALUES (:userid, :tenantid, :dataset_id, :column_id, :line_id, :val);
                #             """
                #     with self.session_scope() as session:
                #         try:
                #             #session.execute(text(query),data_to_insert) # TODO verifier que ça fonctionne
                #             for record in data_to_insert:
                #                         session.execute(text(query), {
                #                             'userid': record[0],
                #                             'tenantid': record[1],
                #                             'dataset_id': record[2],
                #                             'column_id': record[3],
                #                             'line_id': record[4],
                #                             'val': record[5]
                #                         })
                #         except SQLAlchemyError as e:
                #             raise e

        except Exception as e:
                print(f"Error storing dataset: {e}")
                return None
        print("POSTGRES id", dataset_id)
        return dataset_id

    def get_list_datasets(self, userid:int, tenantid:int, offset:int,limit:int) -> List[Dataset]:
        query = "SELECT * FROM datasets WHERE userid = :userid AND tenantid = :tenantid ORDER BY created_at OFFSET :offset LIMIT :limit;"
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

    def get_dataset_metadata(self,id:int, userid:int, tenantid:int) -> List[Metadata]:
        query1 = "SELECT * FROM datasets WHERE id=:id AND userid = :userid AND tenantid = :tenantid;"
        query2 = "SELECT * FROM metadata WHERE dataset_id = :dataset_id AND userid = :userid AND tenantid = :tenantid ORDER BY column_id;"
        with self.session_scope() as session:
            try:
                dataset = session.execute(text(query1), {
                    'id':id,
                    'userid': userid,
                    'tenantid': tenantid,
                }).mappings().fetchone()
                if dataset.deleted_at:
                    print("deleted")
                    return # if the dataset was deleted we don't return anything (TODO)

                metadatas = session.execute(text(query2), {
                    'dataset_id':id,
                    'userid': userid,
                    'tenantid': tenantid,
                }).mappings().fetchall()
                print("METADATAS: ",metadatas)
                result = [
                    Metadata(
                        userid=metadata.userid,
                        tenantid=metadata.tenantid,
                        dataset_id=metadata.dataset_id,
                        column_id= metadata.column_id,
                        column_name=metadata.column_name,
                        type_= metadata.type_
                    ) for metadata in metadatas ]

                return result
            except Exception as e:
                print(f"Error fetching metadata: {e}")
                return None



    def get_dataset_content(self,id:int, userid:int, tenantid:int, offset:int=None,limit:int=None) -> List[List[str]]: # TODO pagination
        # we order by column and line number
        query1 = "SELECT * FROM datasets WHERE id=:id AND userid = :userid AND tenantid = :tenantid;"
        query2 = "SELECT * FROM dataset_content WHERE dataset_id = :dataset_id AND userid = :userid AND tenantid = :tenantid ORDER BY column_id,line_id OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            try:
                dataset = session.execute(text(query1), {
                                'id':id,
                                'userid': userid,
                                'tenantid': tenantid,
                            }).mappings().fetchone()

                if not dataset or dataset.deleted_at:
                    print("Error: Dataset not found (might have been deleted).")
                    return None # if the dataset was deleted we don't return anything (TODO)

                rows = session.execute(text(query2), {
                    'dataset_id': id,
                    'userid': userid,
                    'tenantid': tenantid,
                    'offset':offset,
                    'limit':limit
                }).mappings().fetchall() # get all values corresponding to dataset name and user id

                if not rows:
                    print("Error: No data found in the dataset.")
                    return None

                columns = defaultdict(list)
                for row in rows:
                    columns[row.column_id].append(row.val) # it is already sorted
                columns_as_lists = list(columns.values())
                return columns_as_lists
                # # Fetch the column names
                # metadata_query = """
                #     SELECT column_id, type_ FROM metadata WHERE dataset_id = :id AND userid = :userid AND tenantid = :tenantid ORDER BY column_id;
                # """
                # metadata = session.execute(text(metadata_query), {
                #                                 'dataset_id':dataset_id,
                #                                 'userid': userid,
                #                                 'tenantid': tenantid,
                #                             }).mappings().fetchall()
                # if not metadata:
                #         print("Error: No metadata found for the dataset.")
                #         return None
                # # Create a dictionary to map column_id to column name
                # column_names = {col_id: f"Column_{col_id}" for col_id, _ in metadata}

                # # Create a dictionary to hold the data by columns
                # data_dict = {column_names[col_id]: [] for col_id, _ in metadata}

                # # Populate the data dictionary with values
                # max_line = max(row[1] for row in rows)
                # for col_id in column_names.keys():
                #     data_dict[column_names[col_id]] = [''] * (max_line + 1)

                # for col_id, line, value in rows:
                #     data_dict[column_names[col_id]][line] = value
                # # Create the DataFrame
                # df = pd.DataFrame(data_dict)
                # columns_list = [df[col].astype(str).tolist() for col in df.columns]
                # return columns_list
            except Exception as e:
                print(f"Error fetching dataset: {e}")
                return None



    def delete_dataset(self,id:int,userid:int, tenantid:int) -> bool:
        query = """UPDATE datasets
                SET deleted_at = NOW()
                WHERE id = :id AND userid = :userid AND tenantid = :tenantid
                """
        with self.session_scope() as session:
            try:
                session.execute(text(query), {
                    'id': id,
                    'userid': userid,
                    'tenantid': tenantid,
                }) # TODO mappings ? fetchall? qu'est ce que ça retourne?


            except Exception as e:
                print(f"Error deleting dataset: {e}")
                return False

        return True



    def transform_dataset(self,userid:int,tenantid:int,dataset_id:int,config_id:int) -> str:
        # first get the config
        query_config = "SELECT * FROM config_generator WHERE id=:id AND userid = :userid AND tenantid = :tenantid;"
        with self.session_scope() as session:
            try:
                dataset =  self.get_dataset_content(dataset_id, userid, tenantid)
                config = session.execute(text(query_config), {
                    'id': config_id,
                    'userid': userid,
                    'tenantid': tenantid,
                }).mappings().fetchone()
                # check dataset
                if (not dataset ):
                    print("Error: Dataset not found.")
                    return None
                # check if config with this id exists
                if (not config):
                    print("Error: Config not found.")
                    return None

                # if no transformation was selected
                print("CONFIG:",config)
                if (not config.hasscramblefield and not config.hasdateshift and
                    not config.hassubfieldlist and not config.hassubfieldregex):
                    print("No transformation was selected")
                    return None

                # parse dataset depending on transformation
                new_dataset = dataset
                if (config.hasscramblefield):
                    new_dataset = self.scramble_fields(new_dataset,dataset_id, config.scramblefield_fields)

                if (config.hasdateshift):
                    print("shift dates")
                    new_dataset = self.shift_dates(userid,tenantid,new_dataset, dataset_id,config.dateshift_lowrange, config.dateshift_highrange)


            except Exception as e:
                print(f"Error transforming dataset: {e}")
                return False

        return new_dataset

# ---------------- utils -------------------------------------------- #

    # Function to shift a list of dates by n days
    def shift_date_col(self,date_list: List[str], n: int) -> List[str]:
        shifted_dates = []
        for date_str in date_list:
            date_obj = parser.parse(date_str)  # Automatically detect and parse the date string
            shifted_date_obj = date_obj + timedelta(days=n)  # Shift the date by n days
            shifted_date_str = shifted_date_obj.strftime("%Y-%m-%d")  # Convert back to string in desired format
            shifted_dates.append(shifted_date_str)
        return shifted_dates

    def shift_dates(self, userid:int,tenantid:int,new_dataset: List[List[str]], dataset_id:int,lowrange:int,highrange:int):
        metadata_list : List[Metadata] = self.get_dataset_metadata(dataset_id,userid,tenantid)
        if (not metadata_list):
            print("No metadata found for this dataset")
            return None
        date_column_ids = [metadata.column_id for metadata in metadata_list if metadata.type_ == "date"]
        random_shift = random.randint(lowrange, highrange)
        for col_id in date_column_ids:
            print("Old date column: ", new_dataset[col_id])
            new_dataset[col_id] = self.shift_date_col(new_dataset[col_id], random_shift)
            print("New date column: ", new_dataset[col_id])

        return new_dataset
