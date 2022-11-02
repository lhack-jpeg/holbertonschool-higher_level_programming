-- Task 1: Root user
-- Creates a user for the server, with all privileges and sets password
CREATE USER IF NOT EXISTS
       'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
