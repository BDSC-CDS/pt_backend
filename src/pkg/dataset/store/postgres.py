from io import StringIO
from typing import List
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.config_generator.model.config_generator import ConfigGenerator
from src.pkg.dataset.model.dataset import Dataset,Metadata,Dataset_content
import csv
from collections import defaultdict
import json
import random
import string
from datetime import datetime, timedelta
from dateutil import parser
from sqlalchemy import text, bindparam
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy.types import String
from src.pkg.config_generator.store.postgres import ConfigGeneratorStore

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
                csv_reader = csv.reader(csvfile)
                headers = next(csv_reader)  # Read the header row

                column_data = [[] for _ in headers]
                for row in csv_reader:
                    for col_index, value in enumerate(row):
                        column_data[col_index].append(value)

                column_types = json.loads(types)
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
                next(csv_reader)  # Skip the header row
                for line_number, row in enumerate(csv_reader):
                    for column_id, value in enumerate(row):
                        # Batch insert every 1000 rows TODO
                        query = """
                            INSERT INTO dataset_content (userid, tenantid, dataset_id, column_id, line_id, val)
                            VALUES (:userid, :tenantid, :dataset_id, :column_id, :line_id, :val);
                        """
                        with self.session_scope() as session:
                            try:

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

        except Exception as e:
                print(f"Error storing dataset: {e}")
                return None
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
        try:
            dataset =  self.get_dataset_content(dataset_id, userid, tenantid)
            # get the configuration
            config_store = ConfigGeneratorStore(self.db)
            config : ConfigGenerator = config_store.get_config(userid,tenantid,config_id)

            # check dataset
            if (not dataset ):
                raise Exception("Error: Dataset not found.")
            # check if config with this id exists
            if (not config):
                raise Exception("Error: Config not found.")

            # if no transformation was selected
            if (not config.hasScrambleField and not config.hasDateShift and
                not config.hassubFieldList and not config.hassubFieldRegex):
                raise Exception("No transformation was selected")

            # parse dataset depending on transformation
            new_dataset = dataset
            metadata_list : List[Metadata] = self.get_dataset_metadata(dataset_id,userid,tenantid)
            if (not metadata_list):
                raise Exception("No metadata found for this dataset")

            if (config.hasScrambleField):
                if not config.scrambleField_fields:
                    raise Exception("No fields given to scramble.")
                new_dataset = self.scramble_fields(new_dataset, metadata_list, dataset_id, config.scrambleField_fields)

            if (config.hasDateShift):
                if not config.dateShift_lowrange or not config.dateShift_highrange:
                    raise Exception("Please provide both ranges.")
                new_dataset = self.shift_dates(new_dataset, metadata_list,config.dateShift_lowrange, config.dateShift_highrange)

            if (config.hassubFieldList):
                if not config.subFieldList_field or not config.subFieldList_substitute or not config.subFieldList_replacement:
                    raise Exception("Missing parameters for the substitution.")
                new_dataset = self.substitute_field(new_dataset, metadata_list, config.subFieldList_field, config.subFieldList_substitute, config.subFieldList_replacement)


            # store the new dataset
            # Generate headers from metadata
            headers = ','.join(f'"{m.column_name}"' for m in metadata_list)
            data_rows = list(zip(*new_dataset))
            csv_rows = [headers] + [','.join(f'"{item}"' for item in row) for row in data_rows]
            csv_string = '\n'.join(csv_rows)
            types_dict = {meta.column_name: meta.type_ for meta in metadata_list}
            types = json.dumps(types_dict)
            new_dataset_id = self.store_dataset(userid,tenantid,"dataset "+str(dataset_id)+ " transformed",csv_string,types)
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

    def shift_dates(self, new_dataset: List[List[str]], metadata_list:List[Metadata],lowrange:int,highrange:int):
        if lowrange == highrange == 0:
            raise ValueError("Both range limits are zero; a non-zero shift cannot be generated.")

        date_column_ids = [metadata.column_id for metadata in metadata_list if metadata.type_ == "date"]
        random_shift = random.randint(lowrange, highrange)
        while random_shift == 0:
            random_shift = random.randint(lowrange, highrange)

        for col_id in date_column_ids:
            new_dataset[col_id] = self.shift_date_col(new_dataset[col_id], random_shift)

        return new_dataset

    def update_metadata_type(self,dataset_id:int, new_type:str, columns:List[str]):
        query = "UPDATE metadata SET type_ = :new_type WHERE dataset_id = :dataset_id AND column_name = ANY (:fields);"

        with self.session_scope() as session:
            try:
                session.execute(text(query), {
                    'dataset_id':dataset_id,
                    'new_type':new_type,
                    'fields': columns
                })

            except Exception as e:
                print(f"Error updating metadata: {e}")
                return False
        return True


    def generate_random_identifier(self):
        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        length = 18
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string



    def scramble_fields(self,new_dataset: List[List[str]], metadata_list:List[Metadata], dataset_id:int, scramble_fields : List[str]):
        column_indices = {meta.column_name: meta.column_id for meta in metadata_list if meta.column_name in scramble_fields}
        # Replace each specified field's value with a unique identifier
        for col_name, col_index in column_indices.items():
            for i in range(len(new_dataset[col_index])):
                new_dataset[col_index][i] = self.generate_random_identifier()

        # update the metadata types to string for these columns
        try:
            result = self.update_metadata_type(dataset_id,'string',list(column_indices.keys()))
        except:
            raise Exception("The updating of the metadata did not work")

        if not result:
            raise Exception("The updating of the metadata did not work")

        return new_dataset


    def substitute_field(self, new_dataset: List[List[str]], metadata_list:List[Metadata], subFieldList_field : str, subFieldList_substitute: List[str], subFieldList_replacement:str):
        print("subfieldlist field: ", subFieldList_field)

        for metadata in metadata_list:
            print("metadata name and id: ", metadata.column_name, metadata.column_id)
            if metadata.column_name == subFieldList_field:
                    print("yeah they are equal")
                    column_id = metadata.column_id
                    break

        target_column = new_dataset[column_id]
        target_column[:] = [subFieldList_replacement if value in subFieldList_substitute else value for value in target_column]

        return new_dataset
