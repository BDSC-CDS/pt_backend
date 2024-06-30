ALTER TABLE questionnaire_versions
ADD COLUMN published BOOLEAN default false;

-- ALTER TABLE config_generator
-- ADD CONSTRAINT config_generator_fk FOREIGN KEY (userid) REFERENCES users(id);
