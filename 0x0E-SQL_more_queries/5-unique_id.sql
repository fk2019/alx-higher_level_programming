-- create unique_id table with a unique and default id
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
