-- Rename table
ALTER TABLE IF EXISTS config_generator RENAME TO transform_config;

-- Alter columns
ALTER TABLE IF EXISTS transform_config RENAME COLUMN config_name TO name;
ALTER TABLE IF EXISTS transform_config RENAME COLUMN created_at TO createdat;
ALTER TABLE IF EXISTS transform_config RENAME COLUMN deleted_at TO deletedat;
ALTER TABLE IF EXISTS transform_config ADD COLUMN updatedat TIMESTAMP WITHOUT TIME ZONE;
UPDATE transform_config SET updatedat = createdat;
ALTER TABLE transform_config ALTER COLUMN updatedat SET NOT NULL;
ALTER TABLE transform_config ALTER COLUMN updatedat SET DEFAULT now();

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

CREATE TABLE IF NOT EXISTS transform_config_scramble_fields (
    id SERIAL PRIMARY KEY,
    config_id INTEGER NOT NULL,
    field TEXT NOT NULL,
    createdat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    updatedat TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    deletedat TIMESTAMP WITHOUT TIME ZONE NULL,

    CONSTRAINT transform_config_scramble_fields_fk FOREIGN KEY (config_id) REFERENCES transform_config(id)
);

CREATE TABLE IF NOT EXISTS transform_config_sub_field_list (
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

CREATE TABLE IF NOT EXISTS transform_config_sub_field_regex (
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
WHERE hasDateShift = TRUE
    AND dateShift_lowrange IS NOT NULL
    AND dateShift_highrange IS NOT NULL;

INSERT INTO transform_config_scramble_fields (config_id, field, createdat, updatedat)
SELECT id, UNNEST(string_to_array(scrambleField_fields, ',')) AS field, createdat, updatedat
FROM transform_config
WHERE hasScrambleField = TRUE
    AND scrambleField_fields IS NOT NULL;

INSERT INTO transform_config_sub_field_list (config_id, name, field, substitute_list, replacement, createdat, updatedat)
SELECT id, 'subfieldlist', subfieldlist_field, subfieldlist_substitute, subfieldlist_replacement, createdat, updatedat
FROM transform_config
WHERE hassubfieldlist = TRUE
    AND subfieldlist_field IS NOT NULL
    AND subfieldlist_substitute IS NOT NULL
    AND subfieldlist_replacement IS NOT NULL;

INSERT INTO transform_config_sub_field_regex (config_id, name, field, regex, replacement, createdat, updatedat)
SELECT id, 'subfieldregex', subfieldregex_field, subfieldregex_regex, subfieldregex_replacement, createdat, updatedat
FROM transform_config
WHERE hassubfieldregex = TRUE
    AND subfieldregex_field IS NOT NULL
    AND subfieldregex_regex IS NOT NULL
    AND subfieldregex_replacement IS NOT NULL;

-- Drop old columns
ALTER TABLE transform_config
DROP COLUMN IF EXISTS hasScrambleField,
DROP COLUMN IF EXISTS hasDateShift,
DROP COLUMN IF EXISTS hassubfieldlist,
DROP COLUMN IF EXISTS hassubfieldregex,
DROP COLUMN IF EXISTS scrambleField_fields,
DROP COLUMN IF EXISTS dateShift_lowrange,
DROP COLUMN IF EXISTS dateShift_highrange,
DROP COLUMN IF EXISTS subfieldlist_field,
DROP COLUMN IF EXISTS subfieldlist_substitute,
DROP COLUMN IF EXISTS subfieldlist_replacement,
DROP COLUMN IF EXISTS subfieldregex_field,
DROP COLUMN IF EXISTS subfieldregex_regex,
DROP COLUMN IF EXISTS subfieldregex_replacement;