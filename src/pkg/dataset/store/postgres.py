from contextlib import contextmanager
from collections import defaultdict
from datetime import timedelta
from io import StringIO
from typing import List
import csv
import json
import random
import re
import string
from dateutil import parser

from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from src.pkg.dataset.model.dataset import Dataset, Metadata
from src.pkg.transform_config.model.transform_config import TransformConfig
from src.pkg.transform_config.store.postgres import TransformConfigStore

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

    def store_dataset(self, userid:int,tenantid:int, dataset_name:str,dataset: str,types:str,identifiers:str, is_id:str, original_filename: str) -> int:
        # Insert dataset entry and get the generated dataset_id
        dataset_query = """
            INSERT INTO datasets
                (userid, tenantid, dataset_name, original_filename, created_at)
            VALUES
                 (:userid, :tenantid, :dataset_name, :original_filename, NOW())
            RETURNING id;
        """
        dataset_id = 0
        with self.session_scope() as session:
            try:
                result = session.execute(text(dataset_query), {
                    'userid': userid,
                    'tenantid': tenantid,
                    'dataset_name':dataset_name,
                    'original_filename': original_filename
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
            column_identifiers = json.loads(identifiers)

            metadata_to_insert = []
            for column_id, header in enumerate(headers):
                column_type = column_types[header]
                column_identifier = column_identifiers[header]
                column_name = header
                is_id_bool = True if is_id == str(column_name) else False
                metadata_to_insert.append((int(userid), int(tenantid), int(dataset_id), int(column_id), str(column_name), str(column_type), str(column_identifier), is_id_bool))
            query = """
                INSERT INTO metadata (userid, tenantid, dataset_id, column_id, column_name, type_, identifier, is_id)
                VALUES (:userid, :tenantid, :dataset_id, :column_id, :column_name, :type_, :identifier, :is_id);
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
                            'type_': record[5],
                            'identifier':record[6],
                            'is_id': record[7],
                        })
                except SQLAlchemyError as e:
                    raise e

            # # insert data content
            csvfile.seek(0)
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            
            batch_size = 1000  # Define batch size
            values_batch = []  # List to accumulate batch data

            for line_number, row in enumerate(csv_reader):
                for column_id, value in enumerate(row):
                    # Append each row data to the batch list
                    values_batch.append({
                        'userid': userid,
                        'tenantid': tenantid,
                        'dataset_id': dataset_id,
                        'column_id': column_id,
                        'line_id': line_number,
                        'val': value
                    })
                    
                    # Perform batch insert when batch size is reached
                    if len(values_batch) == batch_size:
                        query = """
                            INSERT INTO dataset_content (userid, tenantid, dataset_id, column_id, line_id, val)
                            VALUES (:userid, :tenantid, :dataset_id, :column_id, :line_id, :val);
                        """
                        with self.session_scope() as session:
                            try:
                                session.execute(text(query), values_batch)
                                values_batch = []  # Clear the batch after inserting
                            except SQLAlchemyError as e:
                                raise e

            # Insert any remaining rows that are less than the batch size
            if values_batch:
                query = """
                    INSERT INTO dataset_content (userid, tenantid, dataset_id, column_id, line_id, val)
                    VALUES (:userid, :tenantid, :dataset_id, :column_id, :line_id, :val);
                """
                with self.session_scope() as session:
                    try:
                        session.execute(text(query), values_batch)
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

    def get_dataset_info(self,id:int, userid:int, tenantid:int) -> Dataset:
        query = "SELECT * FROM datasets WHERE id=:id AND userid = :userid AND tenantid = :tenantid;"
        with self.session_scope() as session:
            try:
                dataset = session.execute(text(query), {
                    'id':id,
                    'userid': userid,
                    'tenantid': tenantid,
                }).mappings().fetchone()

                if dataset.deleted_at:
                    raise Exception("Dataset is deleted")

                result = Dataset(
                    userid=userid,
                    tenantid=tenantid,
                    dataset_name=dataset.dataset_name,
                    id=dataset.id,
                    original_filename=dataset.original_filename,
                    created_at=dataset.created_at,
                )

                return result

            except Exception as e:
                print(f"Error fetching info: {e}")
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
                        type_= metadata.type_,
                        identifier=metadata.identifier,
                        is_id=metadata.is_id,
                    ) for metadata in metadatas ]

                return result
            except Exception as e:
                print(f"Error fetching metadata: {e}")
                return None



    def get_dataset_content(self,id:int, userid:int, tenantid:int, offset:int=None,limit:int=None) -> List[List[str]]: # TODO pagination
        # we order by column and line number
        query1 = "SELECT * FROM datasets WHERE id=:id AND userid = :userid AND tenantid = :tenantid;"
        query2 = """SELECT * FROM dataset_content
            WHERE dataset_id = :dataset_id
            AND userid = :userid
            AND tenantid = :tenantid
        """
        query3 = "SELECT COUNT(DISTINCT line_id) as totalRows FROM dataset_content WHERE dataset_id = :dataset_id AND userid = :userid AND tenantid = :tenantid;"

        # Parameters for the query
        params = {
            'dataset_id': id,
            'userid': userid,
            'tenantid': tenantid
        }

        # Add LIMIT and OFFSET if they are provided
        if limit is not None:
            query2 += """
            AND line_id BETWEEN :offset AND (:offset + :limit - 1)
            """
            params['offset'] = offset if offset is not None else 0  # Default to 0 if no OFFSET
            params['limit'] = limit

        query2 += """
            ORDER BY line_id, column_id;
        """
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

                total_rows_result = session.execute(text(query3), params).mappings().fetchone()
                total_rows = total_rows_result['totalrows'] if total_rows_result else 0

                rows = session.execute(text(query2), params).mappings().fetchall() # get all values corresponding to dataset name and user id

                if not rows:
                    print("Error: No data found in the dataset.")
                    return None

                columns = defaultdict(list)

                for row in rows:
                    columns[row.column_id].append(row.val) # it is already sorted

                columns_as_lists = list(columns.values())

                return columns_as_lists, total_rows

            except Exception as e:
                print(f"Error fetching dataset: {e}")
                return None

    def get_identifiers_and_quasi_dataset(self, id: int, userid: int, tenantid: int,offset:int=None,limit:int=None) -> List[List[str]]:
        """
        Get the dataset with only the columns that are marked as 'identifier' or 'quasi-identifier'.
        """
        # Fetch the metadata
        metadata_list = self.get_dataset_metadata(id, userid, tenantid)
        if not metadata_list:
            raise Exception("No metadata found for this dataset")

        # Identify columns that are 'identifier' or 'quasi-identifier'
        identifier_columns = [
            metadata.column_id for metadata in metadata_list
            if metadata.identifier in ('identifier', 'quasi-identifier')
        ]

        if not identifier_columns:
            raise Exception("No identifier or quasi-identifier columns found in the dataset")

        # Fetch the content of the dataset
        dataset_content, n_rows = self.get_dataset_content(id, userid, tenantid,offset,limit)

        # Filter the dataset to include only the relevant columns
        filtered_dataset = [dataset_content[col_id] for col_id in identifier_columns]

        return filtered_dataset,n_rows

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

    def insert_transformation_entry(self, userid, tenantid, new_dataset_id, config_id, scramble_field_cols, date_shift, sub_list_col, sub_regex_col):
        query = """
            INSERT INTO transformations (userid, tenantid, old_dataset_id, config_id, scramble_fields_cols, date_shift, sub_list_col, sub_regex_col)
            VALUES (:userid, :tenantid, :old_dataset_id, :config_id, :scramble_fields_cols, :date_shift, :sub_list_col, :sub_regex_col);
        """

        # Creating a dictionary to store parameters
        params = {
            'userid': userid,
            'tenantid': tenantid,
            'old_dataset_id': new_dataset_id,
            'config_id': config_id,
            'scramble_fields_cols': json.dumps(scramble_field_cols) if scramble_field_cols is not None else None,
            'date_shift': json.dumps(date_shift) if date_shift is not None else None,
            'sub_list_col': json.dumps(sub_list_col) if sub_list_col is not None else None,
            'sub_regex_col': json.dumps(sub_regex_col) if sub_regex_col is not None else None
        }

        with self.session_scope() as session:
            try:
                session.execute(text(query), params)
            except SQLAlchemyError as e:
                raise e

    def transform_dataset(self,userid:int,tenantid:int,dataset_id:int,config_id:int) -> str:
        try:
            # Get the dataset details and content
            dataset_content, n_rows =  self.get_dataset_content(dataset_id, userid, tenantid)
            dataset_info = self.get_dataset_info(dataset_id, userid, tenantid)
            dataset_metadata : List[Metadata] = self.get_dataset_metadata(dataset_id,userid,tenantid)
            if (not dataset_content or not dataset_info or not dataset_metadata):
                raise Exception("Error: unable to retrieve dataset details.")

            # Get the transform configuration
            config_store = TransformConfigStore(self.db)
            config : TransformConfig = config_store.get_transform_config(userid, tenantid, config_id)
            if (not config):
                raise Exception("Error: unable to retrieve config.")

            # Raise error if there is no transformation to perform
            if (not config.dateShift and not config.scrambleField and not config.subFieldListList and not config.subFieldRegexList):
                raise Exception("Error: no transformation to perform.")

            # Parse dataset depending on transformation
            new_dataset = dataset_content
            date_shift, scramble_field_cols, sub_list_col, sub_regex_col = None, None, None, None

            if(config.dateShift):
                if not config.dateShift.lowrange or not config.dateShift.highrange:
                    raise Exception("Please provide both ranges.")
                new_dataset, date_shift = self.shift_dates(new_dataset, dataset_metadata, config.dateShift.lowrange, config.dateShift.highrange)

            if (config.scrambleField):
                if not config.scrambleField.fields:
                    raise Exception("No fields given to scramble.")
                new_dataset, scramble_field_cols = self.scramble_fields(new_dataset, dataset_metadata, dataset_id, config.scrambleField.fields)

            if (config.subFieldListList):
                for subfield in config.subFieldListList:
                    if not subfield.field or not subfield.substituteList or not subfield.replacement:
                        raise Exception("Missing parameters for the substitution.")
                    new_dataset, sub_list_col = self.substitute_field(new_dataset, dataset_metadata, subfield.field, subfield.substituteList, subfield.replacement)

            if (config.subFieldRegexList):
                for subfield in config.subFieldRegexList:
                    if not subfield.field or not subfield.regex or not subfield.replacement:
                        raise Exception("Missing parameters for the substitution.")
                    new_dataset, sub_regex_col = self.substitute_field_regex(new_dataset, dataset_metadata, subfield.field, subfield.regex, subfield.replacement)

            # store the new dataset
            # Generate headers from metadata
            headers = ','.join(f'"{m.column_name}"' for m in dataset_metadata)
            data_rows = list(zip(*new_dataset))
            csv_rows = [headers] + [','.join(f'"{item}"' for item in row) for row in data_rows]
            csv_string = '\n'.join(csv_rows)
            types_dict = {meta.column_name: meta.type_ for meta in dataset_metadata}
            types = json.dumps(types_dict)
            identifiers_dict = {meta.column_name: meta.identifier for meta in dataset_metadata}
            identifiers = json.dumps(identifiers_dict)
            is_id = next((meta.column_name for meta in dataset_metadata if meta.is_id), None)
            print("IS ID TRANSFORM: ", is_id)
            new_dataset_id = self.store_dataset(userid,tenantid,"dataset "+str(dataset_id)+ " transformed",csv_string,types,identifiers,is_id,dataset_info.original_filename)

            # Create transformation entry
            self.insert_transformation_entry(userid, tenantid, new_dataset_id, config_id, scramble_field_cols, date_shift, sub_list_col, sub_regex_col)
            
            return new_dataset_id

        except Exception as e:
            print(f"Error transforming dataset: {e}")
            return False


    def revert_dataset(self,userid:int,tenantid:int,dataset_id:int) -> str:
        query = "SELECT * FROM transformations WHERE old_dataset_id = :dataset_id AND userid = :userid AND tenantid = :tenantid;"
        with self.session_scope() as session:
            try:
                transformation = session.execute(text(query), {
                    'dataset_id':dataset_id,
                    'userid': userid,
                    'tenantid': tenantid,
                }).mappings().fetchone()

                if not transformation:
                    raise Exception("Error: This dataset was not transformed.")

                config_store = TransformConfigStore(self.db)
                config : TransformConfig = config_store.get_transform_config(userid,tenantid,transformation.config_id)
                dataset =  self.get_dataset_content(dataset_id, userid, tenantid)
                dataset_info = self.get_dataset_info(dataset_id, userid, tenantid)

                # check dataset
                if (not dataset):
                    raise Exception("Error: Dataset not found.")

                # Raise error if there is no transformation to perform
                if (not config.dateShift and not config.scrambleField and not config.subFieldListList and not config.subFieldRegexList):
                    raise Exception("Error: This dataset was not transformed.")

                new_dataset = dataset
                metadata_list : List[Metadata] = self.get_dataset_metadata(dataset_id,userid,tenantid)

                if config.scrambleField:
                    new_dataset = self.revert_scramble_field(new_dataset, metadata_list, transformation.scramble_fields_cols, config.scrambleField_fields)
                if config.dateShift:
                    new_dataset = self.revert_date_shift(new_dataset, metadata_list, transformation.date_shift)
                if config.subFieldListList:
                    for subfield in config.subFieldListList:
                        if not subfield.field or not subfield.substituteList or not subfield.replacement:
                            raise Exception("Missing parameters for the substitution.")
                        new_dataset = self.revert_substitute(new_dataset, metadata_list, subfield.field, transformation.sub_list_col)
                if config.subFieldRegexList:
                    new_dataset = self.revert_substitute(new_dataset, metadata_list, config.subFieldRegex_field, transformation.sub_regex_col)

                # store the new dataset
                headers = ','.join(f'"{m.column_name}"' for m in metadata_list)
                data_rows = list(zip(*new_dataset))
                csv_rows = [headers] + [','.join(f'"{item}"' for item in row) for row in data_rows]
                csv_string = '\n'.join(csv_rows)
                types_dict = {meta.column_name: meta.type_ for meta in metadata_list}
                types = json.dumps(types_dict)
                identifiers_dict = {meta.column_name: meta.identifier for meta in metadata_list}
                identifiers = json.dumps(identifiers_dict)
                is_id_dict = {meta.column_name: meta.is_id for meta in metadata_list}
                is_id = json.dumps(is_id_dict)
                new_dataset_id = self.store_dataset(userid,tenantid,"dataset "+str(dataset_id)+ " reverted",csv_string,types,identifiers,is_id,dataset_info.original_filename)

            except Exception as e:
                print(f"Error reverting dataset: {e}")
                return None

        return new_dataset_id

    def change_types_dataset(self,userid:int, tenantid:int,dataset_id:int,new_metadata: List[Metadata]):
        try:
            dataset, n_rows =  self.get_dataset_content(dataset_id, userid, tenantid)
            dataset_info = self.get_dataset_info(dataset_id, userid, tenantid)

            # check dataset
            if (not dataset ):
                raise Exception("Error: Dataset not found.")

            # store the new dataset
            # Generate headers from metadata
            headers = ','.join(f'"{m.column_name}"' for m in new_metadata)
            data_rows = list(zip(*dataset))
            csv_rows = [headers] + [','.join(f'"{item}"' for item in row) for row in data_rows]
            csv_string = '\n'.join(csv_rows)
            types_dict = {meta.column_name: meta.type_ for meta in new_metadata}
            types = json.dumps(types_dict)
            identifiers_dict = {meta.column_name: meta.identifier for meta in new_metadata}
            identifiers = json.dumps(identifiers_dict)
            is_id = next((meta.column_name for meta in new_metadata if meta.is_id), None)
            new_dataset_id = self.store_dataset(userid,tenantid,"dataset "+str(dataset_id)+ " with changed types",csv_string,types,identifiers,is_id,dataset_info.original_filename)

        except Exception as e:
                print(f"Error changing the types of the dataset: {e}")
                return False

        return new_dataset_id

    def update_dataset(self,userid:int, tenantid:int,id:int, new_name:str):
        query = "UPDATE datasets SET dataset_name = :new_name WHERE id = :dataset_id AND userid = :userid AND tenantid = :tenantid;"
        with self.session_scope() as session:
            try:
                session.execute(text(query), {
                    'new_name': new_name,
                    'dataset_id': id,
                    'userid': userid,
                    'tenantid': tenantid,
                })

            except Exception as e:
                print(f"Error renaming dataset: {e}")
                return False

        return True
# ---------------- utils -------------------------------------------- #

    # Function to shift a list of dates by n days
    def shift_date_col(self,date_list: List[str], n: int) -> List[str]:
        shifted_dates = []
        for date_str in date_list:
            if not date_str:
                shifted_dates.append("")
                continue
            date_obj = parser.parse(date_str)  # Automatically detect and parse the date string
            shifted_date_obj = date_obj + timedelta(days=n)  # Shift the date by n days
            shifted_date_str = shifted_date_obj.strftime("%Y-%m-%d")  # Convert back to string in desired format
            shifted_dates.append(shifted_date_str)
        return shifted_dates

    # Perform date shifting on the dataset
    def shift_dates(self, new_dataset: List[List[str]], metadata_list:List[Metadata], lowrange:int, highrange:int):
        if lowrange == highrange == 0:
            raise ValueError("Both range limits are zero; a non-zero shift cannot be generated.")

        date_column_ids = [metadata.column_id for metadata in metadata_list if metadata.type_ == "date"]
        iden_col_id = next((metadata.column_id for metadata in metadata_list if metadata.is_id), None)

        if iden_col_id is None:
            raise ValueError("No ID column found in metadata.")

        id_col = new_dataset[iden_col_id]
        unique_ids = set(id_col)
        id_to_shift = {}

        # Generate a unique random shift for each unique ID
        for unique_id in unique_ids:
            random_shift = random.randint(lowrange, highrange)
            while random_shift == 0:
                random_shift = random.randint(lowrange, highrange)
            id_to_shift[unique_id] = random_shift

        # Apply the shifts to the date columns
        for col_id in date_column_ids:
            for i in range(len(new_dataset[col_id])):
                patient_id = id_col[i]
                print("PATIENT ID: ", patient_id)
                shift_value = id_to_shift[patient_id]
                print("SHIFT VALUE: ", shift_value)
                shifted_date = self.shift_date_col([new_dataset[col_id][i]], shift_value)[0]
                new_dataset[col_id][i] = shifted_date

        return new_dataset, id_to_shift

    # Update the metadata type for specific columns in a dataset
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

    # Generate a random identifier string
    def generate_random_identifier(self):
        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        length = 18
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    # Perform field scrambling on specified fields in the dataset
    def scramble_fields(self, new_dataset: List[List[str]], metadata_list:List[Metadata], dataset_id:int, scramble_fields : List[str]):
        column_indices = {meta.column_name: meta.column_id for meta in metadata_list if meta.column_name in scramble_fields}
        # Replace each specified field's value with a unique identifier
        scramble_field_cols = {}

        for col_name, col_index in column_indices.items():
            # scramble_field_cols[col_name] = new_dataset[col_index].copy()
            for i in range(len(new_dataset[col_index])):
                old_value = new_dataset[col_index][i]

                 # Check if the old_value has already been mapped
                if old_value in scramble_field_cols:
                    new_value = scramble_field_cols[old_value]
                else:
                    new_value = self.generate_random_identifier()
                    scramble_field_cols[old_value] = new_value
                # Update the dataset with the new_value
                new_dataset[col_index][i] = new_value

        # update the metadata types to string for these columns
        try:
            result = self.update_metadata_type(dataset_id,'string',list(column_indices.keys()))
        except:
            raise Exception("The updating of the metadata did not work")

        if not result:
            raise Exception("The updating of the metadata did not work")

        return new_dataset, scramble_field_cols

    # Perform field substitution based on a list of values
    def substitute_field(self, new_dataset: List[List[str]], metadata_list:List[Metadata],  field: str, substitutionList: List[str], replacement:str):
        # get the corresponding column id
        for metadata in metadata_list:
            if metadata.column_name == field:
                column_id = metadata.column_id
                break
        # replace the values in the goal column if they match the substitute values
        target_column = new_dataset[column_id]
        sub_field_col = target_column.copy()
        target_column = [replacement if value in substitutionList else value for value in target_column]

        return new_dataset, sub_field_col

    # Perform field substitution based on a regex pattern
    def substitute_field_regex(self, new_dataset: List[List[str]], metadata_list:List[Metadata], subFieldRegex_field : str, subFieldRegex_regex: str, subFieldRegex_replacement:str):
         # check validity of regex
        try:
            pattern = re.compile(subFieldRegex_regex.rstrip('\n'))
        except:
            raise Exception("The regex is not valid.")

        # get the corresponding column id
        for metadata in metadata_list:
            if metadata.column_name == subFieldRegex_field:
                column_id = metadata.column_id
                break

        # replace the values in the goal column if they match the regex
        original_column = new_dataset[column_id].copy()
        target_column = new_dataset[column_id]
        target_column[:] = [subFieldRegex_replacement if re.search(pattern,value) else value for value in target_column]
        changes_made = original_column != new_dataset[column_id]
        # raise error if nothing matched the regex
        if not changes_made:
            print("RAISING EXCEPTION")
            raise Exception("Nothing matched the regex in the indicated column.")

        return new_dataset, original_column


    def revert_scramble_field(self, new_dataset: List[List[str]], metadata_list:List[Metadata], scramble_fields_cols:str, scramble_cols:List[str]):
        cols_dict = json.loads(scramble_fields_cols)
        # Reverse the dictionary
        reversed_dict = {v: k for k, v in cols_dict.items()}

        column_mapping = {meta.column_name: meta.column_id for meta in metadata_list}
         # Iterate over the dictionary to replace corresponding columns in the dataset
        for col_name, col_id in column_mapping.items():
            if col_name in scramble_cols:
                # iterate over all values in the column and replace with original value
                for i in range(len(new_dataset[col_id])):
                    scrambled_value = new_dataset[col_id][i]
                    original_value = reversed_dict.get(scrambled_value)
                    new_dataset[col_id][i] = original_value
        return new_dataset

    def revert_date_shift(self,new_dataset: List[List[str]], metadata_list: List[Metadata], date_shift : str) :
        date_shift_dict = json.loads(date_shift)
        # get the columns that are dates
        date_column_ids = [metadata.column_id for metadata in metadata_list if metadata.type_ == "date"]
        iden_col_id = next((metadata.column_id for metadata in metadata_list if metadata.is_id), None)

        if iden_col_id is None:
                    raise ValueError("No ID column found in metadata.")

        id_col = new_dataset[iden_col_id]
        # shift back to the old dates
        for col_id in date_column_ids:
            for i in range(len(new_dataset[col_id])):
                patient_id = id_col[i]
                shift_value = date_shift_dict.get(patient_id, 0)  # Get the shift value from the dict
                shifted_date = self.shift_date_col([new_dataset[col_id][i]], -shift_value)[0]  # Reverse the shift
                new_dataset[col_id][i] = shifted_date

        return new_dataset

    def revert_substitute(self, new_dataset: List[List[str]], metadata_list: List[Metadata], field: str, sub_col:str):
        # get the array of old values corresponding to the old column
        old_column = json.loads(sub_col)
        # find the column id to replace
        column_id = None

        for meta in metadata_list:
            if meta.column_name == field:
                column_id = meta.column_id

        if column_id is None:
            raise Exception("This column does not exist.")

        # replace the old column
        new_dataset[column_id] = old_column

        return new_dataset
