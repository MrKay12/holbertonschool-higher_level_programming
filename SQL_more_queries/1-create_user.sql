-- script that creates the MySQL server user user_0d_1
create DATABASE IF not exists hbtn_0c_0;
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT privileges on hbtn_0c_0.* TO 'user_0d_1'@'localhost';