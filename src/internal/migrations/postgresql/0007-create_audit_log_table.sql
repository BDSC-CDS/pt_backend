CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL,
    service TEXT NOT NULL,
    action TEXT NOT NULL,
    body TEXT,
    response TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    error BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE INDEX idx_auditlog_userid_created_at ON audit_logs (userid, created_at);
