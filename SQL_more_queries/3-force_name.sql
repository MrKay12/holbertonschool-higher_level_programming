-- creates the table force_name on your MySQL server.
create table if not exists force_name (
    id INT,
    name VARCHAR(256) not null
);