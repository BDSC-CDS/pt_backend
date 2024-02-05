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
