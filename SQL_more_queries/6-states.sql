--creates the database hbtn_0d_usa and the table states
create DATABASE IF not exists hbtn_0d_usa;
create table if not exists states (
    id INT IDENTITY(1,1) UNIQUE not null PRIMARY KEY,
    name VARCHAR not null(256)
);