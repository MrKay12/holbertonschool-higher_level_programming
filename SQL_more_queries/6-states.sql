--creates the database hbtn_0d_usa and the table states
create DATABASE IF not exists hbtn_0d_usa;
create table if not exists hbtn_0d_usa.states (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) not null
);