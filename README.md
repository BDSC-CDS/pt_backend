# RDeID backend

## Introduction
The privacy toolbox is a one stop privacy platform, offer pseudonymisation, de-identification, anonymisation, synthetic data generation and other tools and services related to data privacy protecting techniques

## Workspace

Either using vscode devcontainer or Docker 

```bash
cd docker 
./build-dev.sh
docker compose up
```

### Running locally

```bash
python3 -m src.cmd.start
```

### Running acceptance tests
```bash
python3 -m unittest discover ./src/tests/acceptance
```


## Developer documentation

To document how to develop within the backend we will implement a concrete service and make backend into a real use case. The goal is to develop a simple medication tracker, so that for instance elderly can save the list of their medication, including the name, the posology and frequency of intake and get reminder for it. 

The service is going to be very basic, just enough to cover most aspect of adding a service to the backend.

### Summary

- We will first add the proto specification that describe our api
- We will add migration controllers and authorization middleware
- We will add migration to create the datastructure in the DB
- We will add the service layer
- And finally we will add the storage layer that interact with the DB.

### .proto specifications

The backend is using the spec first pattern. This mean that the speicifation and documentation of the API is not something that comes after coding the actual api as is usual. The inconvenient of the usual approach is that the specs and documentation tend to always be outdated and an aftertought. Here we write the specification and the backend automatically interpret those and accept an API based on it. Any change in the specs is immediately and without further code reflected in the backend's behavious and in the documentation.

The format used for the specification is [Protocol Buffers](https://protobuf.dev/programming-guides/proto3/), it will allow the backend to support [gRPC](https://grpc.io/docs/what-is-grpc/introduction/) and support http via [annotation](https://cloud.google.com/endpoints/docs/grpc/transcoding) and [documentation](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/customizing_openapi_output/) similarely.

We start from the existing file [`api/proto/v1/user-service.proto`](https://github.com/BDSC-CDS/pt_backend/blob/feat/medication-service/api/proto/v1/user-service.proto). We copy it and remove all message and service. We keep only the imports and headers.

To have a simple but complete API for the medication tracker we need to be able to create a medication, list medications, get a single medication and its details and remove a medication.

Let's start with the create medication. What we want in term of a REST API is a POST call on the route /api/v1/medication for instance with a JSON body looking like that:

```json
{
  "medication": {
    "name": "Paracetamol",
    "dosage": "500mg",
    "frequency": "every day at 09:00"
  }
}
```

As a result we want something that tells us the id of the medication created, for instance:
```json
{
    "result": {
        "id": 1
    }
}
```

We normally don't need the content of the medication since we created it, and we can get it with a subsequent GET query if necessary.
 

For this we create the service and the rpc entrypoing and related messages:

```proto
message CreateMedicationRequest {
    Medication medication = 1;
}
message CreateMedicationReply {
    CreateMedicationResult result = 1;
}
message CreateMedicationResult {
    uint32 id = 1;
}

service MedicationService {
    rpc CreateMedication(CreateMedicationRequest) returns (CreateMedicationReply) {
        option (google.api.http) = {
            post: "/api/v1/medication"
            body: "*"
        };
        option (grpc.gateway.protoc_gen_openapiv2.options.openapiv2_operation) = {
            summary: "Create a medication";
            description: "This endpoint creates a medication, and its schedule";
            tags: "Medication";
            extensions: {
                key: "x-openapi-router-controller";
                value {string_value: "medication_controller"};
            };
        };
    };
}
```

Note the summary, description of the openapi extention. This will allow us to autogenerate the documentation.

The x-openapi-router-controller is necessary to autogenerate the server code and need to always be the same (only the name of the controller need to change matching the file).

In a separate file we describe the medication entity (we do this to simplify imports if other services need it).

```proto
message Medication {
    uint32 id = 1;

    uint32 user_id = 2;
    string name = 3;
    string dosage = 4;
    string frequency = 5;

    google.protobuf.Timestamp createdAt = 6;
    google.protobuf.Timestamp updatedAt = 7;
}
```

We do the same for the GET (single and list) and DELETE.

For the list we also need not to forget to have pagination parameters so that we don't have scaling issue if the number of element in the database become to big.

```proto
message ListMedicationRequest {
    uint32 offset = 1;
    uint32 limit = 2;
}
```

This gives us the [service](https://github.com/BDSC-CDS/pt_backend/blob/feat/medication-service/api/proto/v1/medication-service.proto) and the [entitiy](https://github.com/BDSC-CDS/pt_backend/blob/feat/medication-service/api/proto/v1/medication.proto)


### running the generator

The code generator takes all updated proto files and creates for us the server code, client code (for the tests) and the documentation.

```bash
./scripts/generate-protos.sh
```

This create a lot of autogenerated files that can all be [commited](https://github.com/BDSC-CDS/pt_backend/commit/8471d0246fd113f15e53a10b5480489eebc54273#diff-2cc4e0ee606b63df9fdd687d085b73fd2ac8f851cdb8b2d1cf56cb8a7797ce26).

The documenation is generated [here](https://github.com/BDSC-CDS/pt_backend/blob/feat/medication-service/api/openapiv2/v1-tags/apis.swagger.yaml). And can be visualized with the [swagger editor](https://editor.swagger.io/) for instance.

![image](doc/medication-service-openapi.png)
![image](doc/medication-service-openapi-detail.png)

The script normally can run anywhere without dependencies but if necesary a development docker container or vs code devcontainer are provided. 

###  Add the medication controller

Now the server part that parse answer is autogenerated but we still need to explain to the server which part of the code handle the query. This part of the code is the controller where we make sure that the request not only match the specification, but makes sense, we also transform the format from the query to the autogenerated class to our own internal format.

First let's just create the class that match the required interface (the interface required by the autogenerated code can be found [here](https://github.com/BDSC-CDS/pt_backend/blob/feat/medication-service/src/internal/api/server_template/controllers/medication_controller.py)). Note that if the interface does not conform (miss a function or has a wrong type, the server won't start).

first we only crate the class without the content.

```python
# src/internal/api/controllers/medication_controller.py
from server_template.models import TemplatebackendCreateMedicationReply
from server_template.models import TemplatebackendCreateMedicationResult
from server_template.models import TemplatebackendCreateMedicationRequest
from server_template.models import TemplatebackendDeleteMedicationReply
from server_template.models import TemplatebackendDeleteMedicationResult
from server_template.models import TemplatebackendGetMedicationReply
from server_template.models import TemplatebackendGetMedicationResult
from server_template.models import TemplatebackendListMedicationReply
from server_template.models import TemplatebackendListMedicationResult

class MedicationController:
    def __init__(self, config, medication_service):
        self.config = config
        self.authentication_service = medication_service

    def medication_service_create_medication(self, user, body: TemplatebackendCreateMedicationRequest):
        return TemplatebackendCreateMedicationReply(TemplatebackendCreateMedicationResult())

    def medication_service_delete_medication(self, user, id: str):
        return TemplatebackendDeleteMedicationReply(TemplatebackendDeleteMedicationResult())

    def medication_service_get_medication(self, user, id: int):
        # medication = TemplatebackendMedication()

        return TemplatebackendGetMedicationReply(TemplatebackendGetMedicationResult())

    def medication_service_list_medication(self, user, offset: int=None, limit: int=None):
        return TemplatebackendListMedicationReply(TemplatebackendListMedicationResult())
```

We also need to provide the controller to the server. (The provider allows to do dependency injection for testing). 

For this we simply copy one of the existing provider, for instance user provider and leave the service and store as None initially.

```python
# src/internal/cmd/provider/medication.py
import src.internal.api.server_template.controllers.medication_controller as connexion_medication_controller
import src.internal.api.controllers.medication_controller as internal_medication_controller
# import src.internal.api.controllers.middleware.medication_authorization as medication_controller_authorization
# from src.pkg.medication.service.medication import MedicationService
# from src.pkg.medication.store.postgres import MedicationStore as PostgresMedicationStore
from .config import provide_config
from .db import provide_db_type, provide_db

medication_controller = None
medication_service = None
medication_store = None

def provide_medication_controller():
    global medication_controller

    if medication_controller is not None:
        return medication_controller

    controller = internal_medication_controller.MedicationController(provide_config(), provide_medication_service())
    # controller = medication_controller_authorization.MedicationControllerAuthentication(controller)
    medication_controller = connexion_medication_controller.MedicationController(controller)

    return medication_controller

def provide_medication_service():
    global medication_service

    if medication_service is not None:
        return medication_service

    # medication_service = MedicationService(provide_medication_store())

    return medication_service

def provide_medication_store():
    global medication_store

    if medication_store is not None:
        return medication_store

    tpe = provide_db_type()

    if tpe == "postgres":
        # medication_store = PostgresMedicationStore(provide_db())
        pass
    else:
        raise NotImplementedError("datastore type " + tpe + " is not implemented")


    return medication_store
```

Finally pass the controller to the server

```python
# src/internal/cmd/provider/controllers.py
from .medication import provide_medication_controller

# ...

controllers['medication_controller'] = provide_medication_controller()

```

### authorization middelware
Again using the interface checking mechanisme we can make sure not to forget to add an authorization check when we add a route. But we need to add the auth middleware. It again has the same interface as the controller.

```python
# src/internal/api/controllers/middleware/medication_authorization.py

from server_template.models import TemplatebackendCreateMedicationRequest
from src.internal.api.controllers.medication_controller import MedicationController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class MedicationControllerAuthentication():
    def __init__(self, next: MedicationController):
        self.next = next
        implements_interface(MedicationController, MedicationControllerAuthentication)

    def medication_service_create_medication(self, user, body: TemplatebackendCreateMedicationRequest):
        if not is_authenticated(user):
            return None, 403

        return self.next.medication_service_create_medication(user, body)

    def medication_service_delete_medication(self, user, id: str):
        if not is_authenticated(user):
            return None, 403

        return self.next.medication_service_delete_medication(user, id)

    def medication_service_get_medication(self, user, id: int):
        if not is_authenticated(user):
            return None, 403

        return self.next.medication_service_get_medication(user, id)

    def medication_service_list_medication(self, user, offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403

        return self.next.medication_service_list_medication(user, offset, limit)
```

And plug it in the provider:


```python
# src/internal/cmd/provider/medication.py
import src.internal.api.controllers.middleware.medication_authorization as medication_controller_authorization

# ...

controller = medication_controller_authorization.MedicationControllerAuthentication(controller)

```

### Migration

We need to write the SQL (Postgres flavor) of the migration file. Here to plumbing necessary. Creating the file is sufficient that in the next run of the backend, it will be executed.

```sql
--- src/internal/migrations/postgresql/0002-medications.sql

CREATE TABLE IF NOT EXISTS medication (
	id SERIAL PRIMARY KEY,
	tenantid INT NOT NULL,

    userid INT NOT NULL,
	name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    frequency TEXT NOT NULL,

    createdat TIMESTAMP NOT NULL DEFAULT now(),
    updatedat TIMESTAMP NOT NULL DEFAULT now(),
    deletedat TIMESTAMP,

	CONSTRAINT usercon FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE INDEX idx_medication_tenantid_userid_createdat ON medication (tenantid, userid, createdat);
```

### Model

We need to represent a medication in a format native to Python. A dataclass. This is our internal (or business) data model. The services only accept data with this model. All other format need to be converted to it before feeding it to the service and back to communicate with api, clients, store etc...

```python
# src/pkg/medication/model/medication.py

import datetime
from dataclasses import dataclass

@dataclass
class Medication:
    id: int = None

    tenantid: int = 0
    userid: int = 0
    name: str = ""
    dosage: str = ""
    frequency: str = ""

    createdat: datetime.datetime
    updatedat: datetime.datetime
    deletedat: datetime.datetime = None


```

### Store layer

To communicate with the database, we need to write the python and SQL queries. We abstract away the implementation detail related to Postgres to a separate store file.

That way, if we want to swap DB we only need to reimplement store file. The rest of our system being independant from the actual DB chosed.

```python
# src/pkg/medication/store/postgres.py

from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.medication.model.medication import Medication


class MedicationStore:
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

    def create_medication(self, medication: Medication) -> Medication:
        medication_query = """
INSERT INTO medication 
    (tenantid, userid, name, dosage, frequency)
VALUES 
    (:tenantid, :userid, :name, :dosage, :frequency) 
RETURNING id;
"""

        with self.session_scope() as session:
            try:
                result = session.execute(text(medication_query), {
                    'tenantid': medication.tenantid,
                    'userid': medication.userid,
                    'name': medication.name,
                    'dosage': medication.dosage,
                    'frequency': medication.frequency,
                }).fetchone()
                medication_id = result[0]

            except SQLAlchemyError as e:
                raise e

            return Medication(id=medication_id)
    
    def list_medications(self, tenantid: int, userid: int, offset: int, limit: int) -> list[Medication] :
        query = "SELECT * FROM medication where tenantid = :tenantid and userid = :userid order by createdat offset :offset limit :limit;"
        with self.session_scope() as session:
            medications = session.execute(text(query), {
                'tenantid': tenantid,
                'userid': userid,
                'offset': offset,
                'limit': limit,
            }).mappings().fetchall()

            ms = [
                Medication(
                    id=medication.id,

                    tenantid=medication.tenantid,
                    userid=medication.userid,

                    name=medication.name,
                    dosage=medication.dosage,
                    frequency=medication.frequency,

                    createdat=medication.createdat,
                    updatedat=medication.updatedat
                ) for medication in medications
            ]

            return ms

```

### The service

Finally we need to create the main part of the application. The service. In the case of the medication tracker, the service is not doing any business logic, only writing and reading the DB. It's extremely straightforward.

```python
# src/pkg/medication/service/medication.py

from src.pkg.medication.model.medication import Medication
from src.pkg.authentication.helper import helper

class MedicationService:
    def __init__(self, medication_store):
        self.medication_store = medication_store

    def create_medication(self, medication: Medication) -> Medication:
        return self.medication_store.create_medication(medication)

    def list_medications(self, tenantid: int, userid: int, offset: int, limit: int) -> Medication:
        medications = self.medication_store.list_medications(tenantid, userid, offset, limit)

        return medications
```


We also need to go back to the provider and uncomment everything so that the actual service load.