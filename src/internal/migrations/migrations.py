import os
import glob
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from . import postgresql

class Migrations:
    def __init__(self, datastore_type: str, datastore_config):
        self.sql = []
        self.migration_table = datastore_config.migration_table_name

        if datastore_type == "postgresql":
            path = os.path.dirname(os.path.abspath(__file__))
            file_names = glob.glob(path + "/postgresql/*.sql")
            file_names = sorted(file_names, key=lambda file_name: file_name.split("/")[-1].replace(".sql", ""))
            print("file names", file_names)

            for file_name in file_names:
                with open(file_name, 'r') as file:
                    data = file.read()
                    self.sql.append({
                        "name": file_name.split("/")[-1].replace(".sql", ""),
                        "sql": data,
                    })

        else:
            raise NotImplementedError("datastore "+ datastore_type + " is not supported")
        
    def migrate(self, db):
        session = Session(db)
        try:

            session.execute(text(postgresql.postgresql_queries["create_migration"](self.migration_table)))

            migrations_applied = session.execute(text(postgresql.postgresql_queries["select_migrations"](self.migration_table))).all()
            migrations_applied = [m[0] for m in migrations_applied]
            
            migration_to_apply = self.list_diff(migrations_applied)

            for m in migration_to_apply:
                session.execute(text(m["sql"]))
                session.execute(text(postgresql.postgresql_queries["insert_migration"](self.migration_table)), params={"migration_name":m["name"]})

            session.commit()

        except:
            session.rollback()
            raise
        finally:
            session.close()

    def list_diff(self, migrations_applied):
        for (idx, m) in enumerate(migrations_applied):
            if idx >= len(self.sql):
                raise Exception("migration previously applied " + m + " not found in migration set")
            if self.sql[idx]["name"] != m:
                raise Exception("migration #" + str(idx + 1) + " should be " + self.sql[idx]["name"] + " not " + m)
        
        migration_to_apply = self.sql[len(migrations_applied):]
        return migration_to_apply

