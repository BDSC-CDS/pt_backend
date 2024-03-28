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
