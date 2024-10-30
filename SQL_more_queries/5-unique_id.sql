-- creates the table unique_id
create table if not exists unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);