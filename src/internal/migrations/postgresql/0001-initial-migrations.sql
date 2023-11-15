CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
	-- tenantid INT64 NULL,

    username  TEXT UNIQUE,
    password  TEXT,
    firstname TEXT,
    lastname  TEXT,
    status    TEXT,
	source	  TEXT,

	totpsecret TEXT,

    createdat TIMESTAMP,
    updatedat TIMESTAMP

	-- CONSTRAINT tenantcon FOREIGN KEY (tenantid) REFERENCES tenants(id)
);

CREATE TABLE IF NOT EXISTS roles (
	id TEXT PRIMARY KEY
);


CREATE TABLE IF NOT EXISTS user_role (
	id SERIAL PRIMARY KEY,

    userid INT64,
	role TEXT,

	CONSTRAINT usercon FOREIGN KEY (userid) REFERENCES users(id),
	CONSTRAINT rolecon FOREIGN KEY (role) REFERENCES roles(id)
);

insert into roles (name) select 'admin' where not exists (select * from roles where name = 'admin');
insert into roles (name) select 'daemon' where not exists (select * from roles where name = 'daemon');