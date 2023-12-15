from . import config
from . import migrations
from sqlalchemy import create_engine
from sqlalchemy import URL
import time


dbs = None

def provide_db_type(datastore_id: str = "template_backend") -> str:
    conf = config.provide_config().config()
        
    for id in conf.storage.datastores:
        if id == datastore_id: 
            return conf.storage.datastores[id].type
    
    return None

def provide_db(datastore_id: str = "template_backend"):
    global dbs
    if dbs is None:
        dbs = {}

        conf = config.provide_config().config()
        
        for id in conf.storage.datastores:
            tpe = conf.storage.datastores[id].type
            if tpe == "postgres":
                dbs[id] = provide_postgres_db(datastore_id, conf.storage.datastores[id])
            else:
                raise NotImplementedError("datastore "+ tpe + " is not supported")
    
    return dbs[datastore_id]

def provide_postgres_db(datastore_id, datastore):

    url_object = URL.create(
        "postgresql+" + datastore.driver,
        username=datastore.username,
        password=datastore.password,
        host=datastore.host,
        database=datastore.database
    )

    debug_mode = False
    if datastore.get("debug_mode"):
        debug_mode = True

    engine = create_engine(url_object, echo=debug_mode)
    engine.connect()

    if datastore_id == "template_backend":
        m = migrations.provide_migrations("postgresql", datastore)
        tries = 3
        for i in range(tries):
            try:
                m.migrate(engine)
            except Exception as e:
                if i < tries - 1:
                    print ("error while migrating, retrying in 3...", e)
                    time.sleep(3)
                    continue
                else:
                    raise e
            break
    
    return engine

