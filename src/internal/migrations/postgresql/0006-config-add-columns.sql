ALTER TABLE config_generator
ADD COLUMN userid INT,
ADD COLUMN tenantid INT;

-- ALTER TABLE config_generator
-- ADD CONSTRAINT config_generator_fk FOREIGN KEY (userid) REFERENCES users(id);
