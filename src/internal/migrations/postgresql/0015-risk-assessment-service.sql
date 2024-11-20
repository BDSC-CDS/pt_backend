CREATE TABLE IF NOT EXISTS risk_assessment (
    id SERIAL PRIMARY KEY, -- Unique identifier for each risk assessment
    tenantid INT NOT NULL, -- Tenant ID for multi-tenancy support
    userid INT NOT NULL,   -- User ID who performed the risk assessment
    dataset_id INT NOT NULL, -- Dataset ID related to the risk assessment
    risk_assessment TEXT NOT NULL, -- Risk assessment result (as a string)

    CONSTRAINT usercon FOREIGN KEY (userid) REFERENCES users(id) -- Foreign key constraint linking to users table
);

CREATE INDEX idx_risk_assessment_tenantid_userid_datasetid 
ON risk_assessment (tenantid, userid, dataset_id);
