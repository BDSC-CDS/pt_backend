CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
	tenantid INT NULL,

    username  TEXT UNIQUE NOT NULL,
    email     TEXT NOT NULL,
    password  TEXT NOT NULL,
    firstname TEXT NOT NULL,
    lastname  TEXT NOT NULL,
    status    TEXT NOT NULL,
	source	  TEXT NOT NULL,

	totpsecret TEXT NOT NULL DEFAULT '',

    createdat TIMESTAMP,
    updatedat TIMESTAMP

	-- CONSTRAINT tenantcon FOREIGN KEY (tenantid) REFERENCES tenants(id)
);

CREATE TABLE IF NOT EXISTS roles (
	id TEXT PRIMARY KEY
);


CREATE TABLE IF NOT EXISTS user_role (
	id SERIAL PRIMARY KEY,

    userid INT,
	role TEXT,

	CONSTRAINT usercon FOREIGN KEY (userid) REFERENCES users(id),
	CONSTRAINT rolecon FOREIGN KEY (role) REFERENCES roles(id)
);

insert into roles (id) select 'admin' where not exists (select * from roles where id = 'admin');
insert into roles (id) select 'daemon' where not exists (select * from roles where id = 'daemon');