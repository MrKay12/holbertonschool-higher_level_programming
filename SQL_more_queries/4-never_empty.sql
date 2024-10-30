-- script that creates the table id_not_null
create table if not exists id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);