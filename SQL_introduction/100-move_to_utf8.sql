-- Task 17: Go to UTF8
-- Convert hbtn_0c_0 to UTF8 along with first_table and first_table.name
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
