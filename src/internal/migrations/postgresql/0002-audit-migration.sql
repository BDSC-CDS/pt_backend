CREATE TABLE IF NOT EXISTS audit_log (
    id SERIAL PRIMARY KEY,
    userid INT,
    service TEXT NOT NULL,
    action TEXT NOT NULL,
    body TEXT NOT NULL,
    response TEXT NOT NULL,
    error BOOLEAN NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT audit_user_fk FOREIGN KEY (userid) REFERENCES users(id)
);


CREATE INDEX idx_auditlog_userid_createdat ON audit_log (userid, created_at);

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