-- creates the table unique_id
create table if not exists id_not_null (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);