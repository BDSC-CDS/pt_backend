from . import config
from sqlalchemy import create_engine
from sqlalchemy import URL
from src.internal.migrations import migrations

migration_instances = {}

def provide_migrations(datastore_type: str, datastore_config):
    global migration_instances

    if migration_instances.get(datastore_type) is not None:
        return migration_instances[datastore_type]
    
    migration_instances[datastore_type] = migrations.Migrations(datastore_type, datastore_config)
    return migration_instances[datastore_type]
    

    
     


