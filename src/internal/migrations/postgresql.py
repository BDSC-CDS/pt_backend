postgresql_queries = {
    "create_migration": lambda migration_table : """
CREATE TABLE IF NOT EXISTS "%s"
(
    migration_name TEXT NOT NULL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL
);
""" % migration_table,
    "select_migrations": lambda migration_table : """
SELECT migration_name FROM "%s" order by created_at;
""" % migration_table,
    "insert_migration": lambda migration_table : """
INSERT INTO "%s" (migration_name, created_at) VALUES
    (:migration_name, now());
""" % migration_table,
}