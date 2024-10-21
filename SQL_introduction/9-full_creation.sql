-- create a table 
create table if not exists second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple row
insert into second_table (id, name, score) values
(1, "Jhon", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);