CREATE TABLE IF NOT EXISTS config_generator (
    id SERIAL PRIMARY KEY,
    userid INT,
    hasScrambleField BOOLEAN,
    hasDateShift BOOLEAN,
    hasSubstituteFieldList BOOLEAN,
    hasSubstituteFieldRegex BOOLEAN,
    scrambleField_fields TEXT,
    dateShift_lowrange INT,
    dateShift_highrange INT,
    substituteFieldList_fields: TEXT,
    substituteFieldList_substitute TEXT,
    substituteFieldList_replacement TEXT,
    substituteFieldRegex_fields TEXT,
    substituteFieldRegex_regex TEXT,
    substituteFieldRegex_replacement TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT config_generator_fk FOREIGN KEY (userid) REFERENCES users(id)
);


CREATE INDEX idx_config_userid_createdat ON audit_log (userid, created_at);
