import json
from contextlib import contextmanager
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from src.pkg.transform_config.model.transform_config import DateShiftConfig, ScrambleFieldConfig, SubFieldListConfig, SubFieldRegexConfig, TransformConfig

class TransformConfigStore:
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

    def create_transform_config(self, userid: int, tenantid: int, transform_config: TransformConfig):
        config_query = """
            INSERT INTO transform_config (userid, tenantid, name, questionnaireid, createdat, updatedat)
            VALUES (:userid, :tenantid, :name, :questionnaireid, now(), now())
            RETURNING id;
            """
        
        dateshift_query = """
            INSERT INTO transform_config_date_shift (config_id, lowrange, highrange, createdat, updatedat)
            VALUES (:config_id, :lowrange, :highrange, now(), now());
            """
        
        scramble_query = """
            INSERT INTO transform_config_scramble_fields (config_id, field, createdat, updatedat)
            VALUES (:config_id, :field, now(), now());
            """
        
        subfieldlist_query = """
            INSERT INTO transform_config_sub_field_list (config_id, name, field, substitute_list, replacement, createdat, updatedat)
            VALUES (:config_id, :name, :field, :substitute_list, :replacement, now(), now());
            """
        
        subfieldregex_query = """
            INSERT INTO transform_config_sub_field_regex (config_id, name, field, regex, replacement, createdat, updatedat)
            VALUES (:config_id, :name, :field, :regex, :replacement, now(), now());
            """
        
        with self.session_scope() as session:
            try:
                result = session.execute(text(config_query), {
                    "userid": userid,
                    "tenantid": tenantid,
                    "name": transform_config.name,
                    "questionnaireid": transform_config.questionnaireid
                }).fetchone()

                config_id = result[0]

                # Insert dateShift config if it exists
                if transform_config.dateShift:
                    session.execute(text(dateshift_query), {
                        "config_id": config_id,
                        "lowrange": transform_config.dateShift.lowrange,
                        "highrange": transform_config.dateShift.highrange
                    })

                # Insert scrambleField config if it exists
                if transform_config.scrambleField:
                    for field in transform_config.scrambleField.fields:
                        session.execute(text(scramble_query), {
                            "config_id": config_id,
                            "field": field
                        })

                # Insert subFieldList config if it exists
                if transform_config.subFieldListList:
                    for subfield in transform_config.subFieldListList:
                        session.execute(text(subfieldlist_query), {
                            "config_id": config_id,
                            "name": subfield.name or "",
                            "field": subfield.field,
                            "substitute_list": ",".join(subfield.substituteList),
                            "replacement": subfield.replacement
                        })

                # Insert subFieldRegex config if it exists
                if transform_config.subFieldRegexList:
                    for subfield in transform_config.subFieldRegexList:
                        session.execute(text(subfieldregex_query), {
                            "config_id": config_id,
                            "name": subfield.name or "",
                            "field": subfield.field,
                            "regex": subfield.regex,
                            "replacement": subfield.replacement
                        })

            except SQLAlchemyError as e:
                print(f"Error creating transform config: {e}")
                raise e

            return config_id


    def list_transform_configs(self, userid:int, tenantid:int, offset: int=0, limit: int=None) -> list[TransformConfig]:
        config_query = "SELECT * FROM transform_config WHERE userid = :userid AND tenantid = :tenantid AND deletedat is NULL ORDER BY createdat OFFSET :offset LIMIT :limit;"
        
        with self.session_scope() as session:
            try:
                configs = session.execute(text(config_query),{
                    "userid":userid,
                    "tenantid":tenantid,
                    "offset":offset,
                    "limit":limit,
                }).mappings().fetchall()

                if not configs:
                    return None
                
                result = []
                for config in configs:
                    # Fetch the dateShift config
                    dateshift_query = "SELECT lowrange, highrange FROM transform_config_date_shift WHERE config_id = :config_id;"
                    dateshift = session.execute(text(dateshift_query), {"config_id": config["id"]}).mappings().fetchone()
                    
                    # Fetch the scrambleField config
                    scramble_query = "SELECT field FROM transform_config_scramble_fields WHERE config_id = :config_id;"
                    scramble = session.execute(text(scramble_query), {"config_id": config["id"]}).mappings().fetchall()

                    # Fetch the subFieldList config
                    subfieldlist_query = "SELECT name, field, substitute_list, replacement FROM transform_config_sub_field_list WHERE config_id = :config_id;"
                    subfieldlist = session.execute(text(subfieldlist_query), {"config_id": config["id"]}).mappings().fetchall()

                    # Fetch the subFieldRegex config
                    subfieldregex_query = "SELECT name, field, regex, replacement FROM transform_config_sub_field_regex WHERE config_id = :config_id;"
                    subfieldregex = session.execute(text(subfieldregex_query), {"config_id": config["id"]}).mappings().fetchall()
                    
                    transform_config = TransformConfig(
                        id=config["id"],
                        userid=config["userid"],
                        tenantid=config["tenantid"],
                        questionnaireid=config["questionnaireid"],
                        name=config["name"],
                        dateShift=DateShiftConfig(
                            lowrange=dateshift["lowrange"],
                            highrange=dateshift["highrange"]
                        ) if dateshift else None,
                        scrambleField=ScrambleFieldConfig(
                            fields=[field["field"] for field in scramble]
                        ) if scramble else None,
                        subFieldListList=[
                            SubFieldListConfig(
                                name=subfield["name"],
                                field=subfield["field"],
                                substituteList=subfield["substitute_list"].split(",") if subfield["substitute_list"] else [],
                                replacement=subfield["replacement"]
                            ) for subfield in subfieldlist
                        ] if subfieldlist else [],
                        subFieldRegexList=[
                            SubFieldRegexConfig(
                                name=subfield["name"],
                                field=subfield["field"],
                                regex=subfield["regex"],
                                replacement=subfield["replacement"]
                            ) for subfield in subfieldregex
                        ] if subfieldregex else [],
                        createdat=config["createdat"],
                        deletedat=config["deletedat"]
                    )
                    result.append(transform_config)

                return result
            
            except SQLAlchemyError as e:
                print(f"Error listing transform configs: {e}")
                raise e


    def get_transform_config(self, userid:int, tenantid:int, config_id:int) -> TransformConfig:
        config_query = "SELECT * FROM transform_config WHERE userid = :userid AND tenantid = :tenantid AND id = :id AND deletedat is NULL"
        with self.session_scope() as session:
            try:
                config = session.execute(text(config_query), {
                    "id":config_id,
                    "userid":userid,
                    "tenantid":tenantid
                }).mappings().fetchone()

                if not config:
                    return None

                # Fetch the dateShift config
                dateshift_query = "SELECT lowrange, highrange FROM transform_config_date_shift WHERE config_id = :config_id"
                dateshift = session.execute(text(dateshift_query), {"config_id": config["id"]}).mappings().fetchone()
                # Fetch the scrambleField config
                scramble_query = "SELECT field FROM transform_config_scramble_fields WHERE config_id = :config_id"
                scramble = session.execute(text(scramble_query), {"config_id": config["id"]}).mappings().fetchall()
                # Fetch the subFieldList config
                subfieldlist_query = "SELECT name, field, substitute_list, replacement FROM transform_config_sub_field_list WHERE config_id = :config_id"
                subfieldlist = session.execute(text(subfieldlist_query), {"config_id": config["id"]}).mappings().fetchall()
                # Fetch the subFieldRegex config
                subfieldregex_query = "SELECT name, field, regex, replacement FROM transform_config_sub_field_regex WHERE config_id = :config_id"
                subfieldregex = session.execute(text(subfieldregex_query), {"config_id": config["id"]}).mappings().fetchall()

                result =TransformConfig(
                    id=config["id"],
                    userid=config["userid"],
                    tenantid=config["tenantid"],
                    questionnaireid=config["questionnaireid"],
                    name=config["name"],
                    dateShift=DateShiftConfig(
                        lowrange=dateshift["lowrange"],
                        highrange=dateshift["highrange"]
                    ) if dateshift else None,
                    scrambleField=ScrambleFieldConfig(
                        fields=[field["field"] for field in scramble]
                    ) if scramble else None,
                    subFieldListList=[
                        SubFieldListConfig(
                            name=subfield["name"],
                            field=subfield["field"],
                            substituteList=subfield["substitute_list"].split(",") if subfield["substitute_list"] else [],
                            replacement=subfield["replacement"]
                        ) for subfield in subfieldlist
                    ] if subfieldlist else [],
                    subFieldRegexList=[
                        SubFieldRegexConfig(
                            name=subfield["name"],
                            field=subfield["field"],
                            regex=subfield["regex"],
                            replacement=subfield["replacement"]
                        ) for subfield in subfieldregex
                    ] if subfieldregex else [],
                    createdat=config["createdat"],
                    deletedat=config["deletedat"]
                )
                        
                return result
            
            except SQLAlchemyError as e:
                print(f"Error getting transform config: {e}")
                raise e


    def delete_transform_config(self, userid: int, tenantid: int, config_id:int):
        config_query = """
        UPDATE transform_config SET deletedat = now()
        WHERE id = :id AND userid = :userid AND tenantid = :tenantid
        """
        
        with self.session_scope() as session:
            try:
                session.execute(text(config_query), {
                    "id": config_id,
                    "userid": userid,
                    "tenantid": tenantid,
                })

                # Delete associated dateShift config
                dateshift_query = """
                UPDATE transform_config_date_shift SET deletedat = now()
                WHERE config_id = :config_id
                """
                session.execute(text(dateshift_query), {"config_id": config_id})
                # Delete associated scrambleField config
                scramble_query = """
                UPDATE transform_config_scramble_fields SET deletedat = now()
                WHERE config_id = :config_id
                """
                session.execute(text(scramble_query), {"config_id": config_id})
                # Delete associated subFieldList config
                subfieldlist_query = """
                UPDATE transform_config_sub_field_list SET deletedat = now()
                WHERE config_id = :config_id
                """
                session.execute(text(subfieldlist_query), {"config_id": config_id})
                # Delete associated subFieldRegex config
                subfieldregex_query = """
                UPDATE transform_config_sub_field_regex SET deletedat = now()
                WHERE config_id = :config_id
                """
                session.execute(text(subfieldregex_query), {"config_id": config_id})
                return True
            
            except Exception as e:
                print(f"Error deleting configuration: {e}")
                raise e


    def export_transform_config(self, userid: int, tenantid: int, config_id: int):
        try:
            config : TransformConfig = self.get_transform_config(userid, tenantid, config_id)
            if config is None:
               return None
            
            result = {}
            if config.dateShift:
                result["dateShift"] = {}
                result["dateShift"]["defaultDateShift"]= {
                    "low_range": config.dateShift.lowrange,
                    "high_range": config.dateShift.highrange
                }
                
            if config.scrambleField:
                result["scrambleField"] = {}
                result["scrambleField"]["defaultScrambling"] = {
                    "applies_to_fields": config.scrambleField.fields
                }

            if config.subFieldListList:
                result["substituteFieldList"] = {}
                for subfield in config.subFieldListList:
                    result["substituteFieldList"][subfield.name] = {
                        "applies_to_field": subfield.field,
                        "substitution_list": subfield.substituteList,
                        "replacement": subfield.replacement
                    }

            if config.subFieldRegexList:
                result["substituteFieldRegex"] = {}
                for subfield in config.subFieldRegexList:
                    result["substituteFieldRegex"][subfield.name] = {
                        "applies_to_field": subfield.field,
                        "regex": subfield.regex,
                        "replacement": subfield.replacement
                    }

            # Return the final JSON output
            return json.dumps(result, indent=4)
        
        except SQLAlchemyError as e:
            print(f"Error exporting transform config: {e}")
            raise e
