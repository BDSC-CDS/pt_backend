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

    def create_config(self, user,config_generator: ConfigGenerator):
        config_query = """
            INSERT INTO config_generator
                (userid, tenantid, config_name, questionnaireid, hasScrambleField, hasDateShift, hassubFieldList, hassubFieldRegex,
                scrambleField_fields, dateShift_lowrange, dateShift_highrange, subFieldList_field,
                subFieldList_substitute, subFieldList_replacement, subFieldRegex_field,
                subFieldRegex_regex,subFieldRegex_replacement, created_at)
            VALUES
                (:userid, :tenantid, :config_name, :questionnaireid, :hasScrambleField, :hasDateShift, :hassubFieldList, :hassubFieldRegex,
                :scrambleField_fields, :dateShift_lowrange, :dateShift_highrange, :subFieldList_field,
                :subFieldList_substitute, :subFieldList_replacement, :subFieldRegex_field,
                :subFieldRegex_regex, :subFieldRegex_replacement, NOW())
            RETURNING id;
            """

        with self.session_scope() as session:
            try:
                result = session.execute(text(config_query), {
                    'userid': user.id,
                    'tenantid': user.tenantid,
                    'config_name': config_generator.config_name,
                    'questionnaireid': config_generator.questionnaireid,
                    'hasScrambleField': config_generator.hasScrambleField,
                    'hasDateShift': config_generator.hasDateShift,
                    'hassubFieldList': config_generator.hassubFieldList,
                    'hassubFieldRegex': config_generator.hassubFieldRegex,
                    'scrambleField_fields': ','.join(config_generator.scrambleField_fields) if config_generator.scrambleField_fields else '',
                    'dateShift_lowrange': config_generator.dateShift_lowrange,
                    'dateShift_highrange': config_generator.dateShift_highrange,
                    'subFieldList_field': config_generator.subFieldList_field,
                    'subFieldList_substitute': ','.join(config_generator.subFieldList_substitute) if config_generator.subFieldList_substitute else '',
                    'subFieldList_replacement': config_generator.subFieldList_replacement,
                    'subFieldRegex_field':config_generator.subFieldRegex_field,
                    'subFieldRegex_regex': config_generator.subFieldRegex_regex,
                    'subFieldRegex_replacement': config_generator.subFieldRegex_replacement
                }).fetchone()

                config_id = result[0]

            except SQLAlchemyError as e:
                raise e

            return config_id

    def get_configs(self,userid:int, tenantid:int) -> list[ConfigGenerator]:
        query = "SELECT * FROM config_generator WHERE userid = :userid AND tenantid = :tenantid ORDER BY created_at;"
        with self.session_scope() as session:
            configs = session.execute(text(query),{
                'userid':userid,
                'tenantid':tenantid,
            }).mappings().fetchall()
            print("CONFIGS: ",configs)
            result = [
                ConfigGenerator(
                    id=config.id,
                    userid=userid,
                    tenantid=config.tenantid,
                    config_name=config.config_name,
                    questionnaireid=config.questionnaireid,
                    hasScrambleField=config.hasscramblefield,
                    hasDateShift=config.hasdateshift,
                    hassubFieldList=config.hassubfieldlist,
                    hassubFieldRegex=config.hassubfieldregex,
                    scrambleField_fields=config.scramblefield_fields.split(","),
                    dateShift_lowrange=config.dateshift_lowrange,
                    dateShift_highrange=config.dateshift_highrange,
                    subFieldList_field=config.subfieldlist_field,
                    subFieldList_substitute=config.subfieldlist_substitute.split(","),
                    subFieldList_replacement=config.subfieldlist_replacement,
                    subFieldRegex_field=config.subfieldregex_field,
                    subFieldRegex_regex=config.subfieldregex_regex,
                    subFieldRegex_replacement=config.subfieldregex_replacement,
                    created_at= config.created_at,
                    deleted_at=config.deleted_at
                ) for config in configs if not config.deleted_at
            ]
            return result

    def get_configs_for_questionnaire(self, userid:int, questionnaireid:int) -> list[ConfigGenerator]:
        query = "SELECT * FROM config_generator WHERE userid=:userid AND questionnaireid = :questionnaireid  ORDER BY created_at;"
        with self.session_scope() as session:
            configs = session.execute(text(query), {
                'userid':userid,
                'questionnaireid': questionnaireid
            }).mappings().fetchall()

            result = [
               ConfigGenerator(
                    id=config.id,
                    userid=userid,
                    tenantid=config.tenantid,
                    config_name=config.config_name,
                    questionnaireid=config.questionnaireid,
                    hasScrambleField=config.hasscramblefield,
                    hasDateShift=config.hasdateshift,
                    hassubFieldList=config.hassubfieldlist,
                    hassubFieldRegex=config.hassubfieldregex,
                    scrambleField_fields=config.scramblefield_fields.split(","),
                    dateShift_lowrange=config.dateshift_lowrange,
                    dateShift_highrange=config.dateshift_highrange,
                    subFieldList_field=config.subfieldlist_field,
                    subFieldList_substitute=config.subfieldlist_substitute.split(","),
                    subFieldList_replacement=config.subfieldlist_replacement,
                    subFieldRegex_field=config.subfieldregex_field,
                    subFieldRegex_regex=config.subfieldregex_regex,
                    subFieldRegex_replacement=config.subfieldregex_replacement,
                    created_at= config.created_at,
                    deleted_at=config.deleted_at
                ) for config in configs if not config.deleted_at
            ]

            return result

    def get_config(self, userid:int, tenantid:int,config_id:int) -> ConfigGenerator:
        query = "SELECT * FROM config_generator WHERE  id =:id AND userid=:userid AND tenantid=:tenantid;"
        with self.session_scope() as session:
            config = session.execute(text(query), {
                'id':config_id,
                'userid':userid,
                'tenantid':tenantid
            }).mappings().fetchone()

            if not config:
                print("No config found")
                return None

            if config.deleted_at:
                    print("deleted")
                    return #TODO

            result =ConfigGenerator(
                    id=config.id,
                    userid=userid,
                    tenantid=config.tenantid,
                    config_name=config.config_name,
                    questionnaireid=config.questionnaireid,
                    hasScrambleField=config.hasscramblefield,
                    hasDateShift=config.hasdateshift,
                    hassubFieldList=config.hassubfieldlist,
                    hassubFieldRegex=config.hassubfieldregex,
                    scrambleField_fields=config.scramblefield_fields.split(","),
                    dateShift_lowrange=config.dateshift_lowrange,
                    dateShift_highrange=config.dateshift_highrange,
                    subFieldList_field=config.subfieldlist_field,
                    subFieldList_substitute=config.subfieldlist_substitute.split(","),
                    subFieldList_replacement=config.subfieldlist_replacement,
                    subFieldRegex_field=config.subfieldregex_field,
                    subFieldRegex_regex=config.subfieldregex_regex,
                    subFieldRegex_replacement=config.subfieldregex_replacement,
                    created_at= config.created_at,
                    deleted_at=config.deleted_at
                )
            return result


    def delete_config(self,user,config_id:int):
        query = """UPDATE config_generator
                SET deleted_at = NOW()
                WHERE id = :id AND userid = :userid AND tenantid = :tenantid
                """
        with self.session_scope() as session:
            try:
                session.execute(text(query), {
                    'id': config_id,
                    'userid': user.id,
                    'tenantid': user.tenantid,
                })


            except Exception as e:
                print(f"Error deleting configuration: {e}")
                return False

        return True
