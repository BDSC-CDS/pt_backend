CREATE TABLE IF NOT EXISTS config_generator (
    id SERIAL PRIMARY KEY,
    userid INT,
    tenantid INT,
    questionnaireid INT,
    hasScrambleField BOOLEAN,
    hasDateShift BOOLEAN,
    hassubFieldList BOOLEAN,
    hassubFieldRegex BOOLEAN,
    scrambleField_fields TEXT,
    dateShift_lowrange INT,
    dateShift_highrange INT,
    subFieldList_fields TEXT,
    subFieldList_substitute TEXT,
    subFieldList_replacement TEXT,
    subFieldRegex_fields TEXT,
    subFieldRegex_regex TEXT,
    subFieldRegex_replacement TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT config_generator_fk FOREIGN KEY (userid) REFERENCES users(id)
    -- CONSTRAINT config_generator_fk FOREIGN KEY (questionnaireid) REFERENCES questionnaire(id)
);


CREATE INDEX idx_config_userid_createdat ON config_generator (userid, created_at);
