CREATE TABLE IF NOT EXISTS audit_log (
    id SERIAL PRIMARY KEY,
    userid INT,
    action TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT audit_user_fk FOREIGN KEY (userid) REFERENCES users(id)
);
