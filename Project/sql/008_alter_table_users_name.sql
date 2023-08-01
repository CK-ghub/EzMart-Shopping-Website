ALTER TABLE IS601_Users
ADD COLUMN firstname varchar(100) not null COMMENT 'First name field of the user';

ALTER TABLE IS601_Users
ADD COLUMN lastname varchar(30) not null COMMENT 'Last name field of the user';