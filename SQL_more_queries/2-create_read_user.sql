-- Task 2: Read User
-- Create a database and user that only has SELECT priv on the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS
       'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- GRANT SELECT PRIVILEGES ONLY FOR USER
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;
