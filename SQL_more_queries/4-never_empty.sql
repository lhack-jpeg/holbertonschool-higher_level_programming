-- Task 4: ID can not be null
-- Create table id_not_null with the id DEFAULT 1
CREATE TABLE IF NOT EXISTS `id_not_null`
(
	id INT DEFAULT(1),
	name VARCHAR(256)
);
