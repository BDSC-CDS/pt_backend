from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.config_generator.model.config_generator import ConfigGenerator

class ConfigGeneratorStore:
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

    def create_config(self, config_generator: ConfigGenerator):
        config_query = """
INSERT INTO config_generator
    (userid, hasScrambleField, hasDateShift, hassubFieldList, hassubFieldRegex,
    scrambleField_fields, dateShift_lowrange, dateShift_highrange, subFieldList_fields,
    subFieldList_substitute, subFieldList_replacement, subFieldRegex_fields,
    subFieldRegex_regex,subFieldRegex_replacement, created_at)
VALUES
    (:userid, :hasScrambleField, :hasDateShift, :hassubFieldList, :hassubFieldRegex,
    :scrambleField_fields, :dateShift_lowrange, :dateShift_highrange, :subFieldList_fields,
    :subFieldList_substitute, :subFieldList_replacement, :subFieldRegex_fields,
    :subFieldRegex_regex, :subFieldRegex_replacement, NOW())
RETURNING id;
"""

        with self.session_scope() as session:
            try:
                result = session.execute(text(config_query), {
                    'userid': config_generator.userid,
                    'hasScrambleField': config_generator.hasScrambleField,
                    'hasDateShift': config_generator.hasDateShift,
                    'hassubFieldList': config_generator.hassubFieldList,
                    'hassubFieldRegex': config_generator.hassubFieldRegex,
                    'scrambleField_fields': ','.join(config_generator.scrambleField_fields),
                    'dateShift_lowrange': config_generator.dateShift_lowrange,
                    'dateShift_highrange': config_generator.dateShift_highrange,
                    'subFieldList_fields': ','.join(config_generator.subFieldList_fields),
                    'subFieldList_substitute': ','.join(config_generator.subFieldList_substitute),
                    'subFieldList_replacement': config_generator.subFieldList_replacement,
                    'subFieldRegex_fields': ','.join(config_generator.subFieldRegex_fields),
                    'subFieldRegex_regex': config_generator.subFieldRegex_regex,
                    'subFieldRegex_replacement': config_generator.subFieldRegex_replacement
                }).fetchone()
                config_id = result[0]

            except SQLAlchemyError as e:
                raise e

            return ConfigGenerator(id=config_id)

    def get_configs(self,offset:int,limit:int) -> list[ConfigGenerator]:
        query = "SELECT * FROM config_generator ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            configs = session.execute(text(query),{
                'offset': offset,
                'limit': limit,
            }).mappings().fetchall()

            result = [
                ConfigGenerator(
                    id=config.id,
                    userid=config.userid,
                    hasScrambleField=config.hasScrambleField,
                    hasDateShift=config.hasDateShift,
                    hassubFieldList=config.hassubFieldList,
                    hassubFieldRegex=config.hassubFieldRegex,
                    scrambleField_fields=config.scrambleField_fields.split(","),
                    dateShift_lowrange=config.dateShift_lowrange,
                    dateShift_highrange=config.dateShift_highrange,
                    subFieldList_fields=config.subFieldList_fields.split(","),
                    subFieldList_substitute=config.subFieldList_substitute.split(","),
                    subFieldList_replacement=config.subFieldList_replacement,
                    suFieldRegex_fields=config.subFieldRegex_fields.split(","),
                    subFieldRegex_regex=config.subFieldRegex_regex,
                    subFieldRegex_replacement=config.subFieldRegex_replacement,
                    created_at= config.created_at
                ) for config in configs
            ]
            return result

    def get_configs_for_user(self, id:int, offset:int, limit:int) -> list[ConfigGenerator]:
        query = "SELECT * FROM config_generator WHERE userid = :userid ORDER BY createdat OFFSET :offset LIMIT :limit;"
        with self.session_scope() as session:
            configs = session.execute(text(query), {
                'userid': id,
                'offset':offset,
                'limit':limit
            }).mappings().fetchall()

            result = [
                ConfigGenerator(
                    id=config.id,
                    userid=config.userid,
                    hasScrambleField=config.hasScrambleField,
                    hasDateShift=config.hasDateShift,
                    hassubFieldList=config.hassubFieldList,
                    hassubFieldRegex=config.hassubFieldRegex,
                    scrambleField_fields=config.scrambleField_fields.split(","),
                    dateShift_lowrange=config.dateShift_lowrange,
                    dateShift_highrange=config.dateShift_highrange,
                    subFieldList_fields=config.subFieldList_fields.split(","),
                    subFieldList_substitute=config.subFieldList_substitute.split(","),
                    subFieldList_replacement=config.subFieldList_replacement,
                    suFieldRegex_fields=config.subFieldRegex_fields.split(","),
                    subFieldRegex_regex=config.subFieldRegex_regex,
                    subFieldRegex_replacement=config.subFieldRegex_replacement,
                    created_at= config.created_at
                ) for config in configs
            ]

            return result
