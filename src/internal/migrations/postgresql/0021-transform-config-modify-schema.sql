-- Rename table
ALTER TABLE config_generator RENAME TO transform_config;

-- Alter columns
ALTER TABLE transform_config RENAME COLUMN config_name TO name;
ALTER TABLE transform_config RENAME COLUMN created_at TO createdat;
ALTER TABLE transform_config RENAME COLUMN deleted_at TO deletedat;
ALTER TABLE transform_config ADD COLUMN updatedat TIMESTAMP WITHOUT TIME ZONE;
UPDATE transform_config SET updatedat = createdat;
ALTER TABLE transform_config ALTER COLUMN updatedat SET NOT NULL;

-- Create sub tables
CREATE TABLE IF NOT EXISTS transform_config_date_shift (
    id SERIAL PRIMARY KEY,
    config_id INTEGER NOT NULL,
    lowrange INTEGER NOT NULL,
    highrange INTEGER NOT NULL,
    createdat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    updatedat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    deletedat TIMESTAMP WITHOUT TIME ZONE NULL,

    CONSTRAINT transform_config_date_shift_fk FOREIGN KEY (config_id) REFERENCES transform_config(id)
);

CREATE TABLE transform_config_scramble_fields (
    id SERIAL PRIMARY KEY,
    config_id INTEGER NOT NULL,
    field TEXT NOT NULL,
    createdat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    updatedat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    deletedat TIMESTAMP WITHOUT TIME ZONE NULL,

    CONSTRAINT transform_config_scramble_fields_fk FOREIGN KEY (config_id) REFERENCES transform_config(id)
);

CREATE TABLE transform_config_sub_field_list (
    id SERIAL PRIMARY KEY,
    config_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    field TEXT NOT NULL,
    substitute_list TEXT NOT NULL,
    replacement TEXT NOT NULL,
    createdat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    updatedat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    deletedat TIMESTAMP WITHOUT TIME ZONE NULL,

    CONSTRAINT transform_config_sub_field_list_fk FOREIGN KEY (config_id) REFERENCES transform_config(id)
);

CREATE TABLE transform_config_sub_field_regex (
    id SERIAL PRIMARY KEY,
    config_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    field TEXT NOT NULL,
    regex TEXT NOT NULL,
    replacement TEXT NOT NULL,
    createdat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    updatedat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    deletedat TIMESTAMP WITHOUT TIME ZONE NULL,

    CONSTRAINT transform_config_sub_field_regex_fk FOREIGN KEY (config_id) REFERENCES transform_config(id)
);

-- Populate tables
INSERT INTO transform_config_date_shift (config_id, lowrange, highrange, createdat, updatedat)
SELECT id, dateShift_lowrange, dateShift_highrange, createdat, updatedat
FROM transform_config
WHERE hasDateShift = TRUE;

INSERT INTO transform_config_scramble_fields (config_id, field, createdat, updatedat)
SELECT id, UNNEST(string_to_array(scrambleField_fields, ',')) AS field, createdat, updatedat
FROM transform_config
WHERE hasScrambleField = TRUE;

INSERT INTO transform_config_sub_field_list (config_id, name, field, substitute_list, replacement, createdat, updatedat)
SELECT id, 'subfieldlist', subfieldlist_field, subfieldlist_substitute, subfieldlist_replacement, createdat, updatedat
FROM transform_config
WHERE hassubfieldlist = TRUE;

INSERT INTO transform_config_sub_field_regex (config_id, name, field, regex, replacement, createdat, updatedat)
SELECT id, 'subfieldregex', subfieldregex_field, subfieldregex_regex, subfieldregex_replacement, createdat, updatedat
FROM transform_config
WHERE hassubfieldregex = TRUE;

-- Drop old columns
ALTER TABLE transform_config
DROP COLUMN hasScrambleField,
DROP COLUMN hasDateShift,
DROP COLUMN hassubfieldlist,
DROP COLUMN hassubfieldregex,
DROP COLUMN scrambleField_fields,
DROP COLUMN dateShift_lowrange,
DROP COLUMN dateShift_highrange,
DROP COLUMN subfieldlist_field,
DROP COLUMN subfieldlist_substitute,
DROP COLUMN subfieldlist_replacement,
DROP COLUMN subfieldregex_field,
DROP COLUMN subfieldregex_regex,
DROP COLUMN subfieldregex_replacement;