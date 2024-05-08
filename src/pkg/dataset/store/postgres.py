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
    (userid, name, data, created_at)
VALUES
    (:userid, :name, :data, NOW())
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

    def get_datasets(self,offset:int,limit:int) -> list[Dataset]:
        query = "SELECT * FROM datasets ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            datasets = session.execute(text(query),{
                'offset': offset,
                'limit': limit,
            }).mappings().fetchall()

            result = [
                Dataset(
                    id=dataset.id,
                    userid=dataset.userid,
                    name=dataset.name,
                    data=dataset.data,
                    created_at= dataset.created_at
                ) for dataset in datasets
            ]
            return result

    def get_datasets_for_user(self, id:int, offset:int, limit:int) -> list[Dataset]:
        query = "SELECT * FROM datasets WHERE userid = :userid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            datasets = session.execute(text(query), {
                'userid': id,
                'offset':offset,
                'limit':limit
            }).mappings().fetchall()

            result = [
               Dataset(
                    id=dataset.id,
                    userid=dataset.userid,
                    name=dataset.name,
                    data=dataset.data,
                    created_at= dataset.created_at
                ) for dataset in datasets
            ]
            return result

    def get_dataset_by_name(self, name:str, offset:int, limit:int) -> list[Dataset]:
        query = "SELECT * FROM datasets WHERE name = :name ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            dataset = session.execute(text(query), {
                'name': name,
                'offset':offset,
                'limit':limit
            }).mappings().fetchone() #only get first result if several with same name TODO ?

            result = Dataset(
                    id=dataset.id,
                    userid=dataset.userid,
                    name=dataset.name,
                    data=dataset.data,
                    created_at= dataset.created_at
                )

            return result
