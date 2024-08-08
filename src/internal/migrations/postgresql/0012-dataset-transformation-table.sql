CREATE TABLE transformations (
    id SERIAL PRIMARY KEY,
    userid INTEGER NOT NULL,
    tenantid INTEGER NOT NULL,
    old_dataset_id INTEGER NOT NULL,
    config_id INTEGER NOT NULL,
    scramble_fields_cols TEXT,
    date_shift INTEGER,
    sub_list_col TEXT,
    sub_regex_col TEXT,

	CONSTRAINT usertransformation FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE INDEX IF NOT EXISTS idx_transformations_userid_old_dataset_id ON transformations (userid, old_dataset_id);
