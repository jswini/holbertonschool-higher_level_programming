-- This script creates a table where there is a default value in the id field
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT '1',
name VARCHAR(256)
)
