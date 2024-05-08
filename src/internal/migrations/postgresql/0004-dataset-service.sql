CREATE TABLE IF NOT EXISTS datasets (
    id SERIAL PRIMARY KEY,
    userid INT,
    name TEXT,
    data JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT dataset_fk FOREIGN KEY (userid) REFERENCES users(id)
);


CREATE INDEX idx_dataset_userid_createdat ON datasets (userid, created_at);
