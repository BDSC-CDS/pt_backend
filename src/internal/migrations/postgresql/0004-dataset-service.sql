 CREATE TABLE IF NOT EXISTS datasets (
    id SERIAL PRIMARY KEY,
    userid INT,
    tenantid INT,
    dataset_name TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP,
    CONSTRAINT datasets_fk FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE INDEX IF NOT EXISTS idx_datasets_userid_createdat ON datasets (userid, created_at); /*TODO do index on name instead of created? */

CREATE TABLE IF NOT EXISTS metadata (
    userid INTEGER,
    tenantid INTEGER,
    dataset_id INTEGER,
    column_id INTEGER,
    column_name TEXT,
    type_ TEXT,
    PRIMARY KEY (dataset_id, column_id),
    CONSTRAINT metadata_fk1 FOREIGN KEY (dataset_id) REFERENCES datasets(id),
    CONSTRAINT metadata_fk2 FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE INDEX IF NOT EXISTS idx_metadata_dataset_id_userid ON metadata (userid, dataset_id, column_id); /*TODO ? */

CREATE TABLE IF NOT EXISTS dataset_content (
    userid INTEGER,
    tenantid INTEGER,
    dataset_id INTEGER,
    column_id INTEGER,
    line_id INTEGER,
    val TEXT,
    PRIMARY KEY (dataset_id, column_id, line_id),
    CONSTRAINT dataset_content_fk1 FOREIGN KEY (dataset_id) REFERENCES datasets(id),
    CONSTRAINT dataset_content_fk2 FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE INDEX IF NOT EXISTS idx_dataset_content_dataset_id_userid ON dataset_content (userid, dataset_id, column_id,line_id); /*TODO ? */
