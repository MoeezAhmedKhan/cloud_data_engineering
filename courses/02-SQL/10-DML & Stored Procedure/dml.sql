-- =========================================================
--         DML (Data Manipulation Language)
-- =========================================================

-- DML is used to work with data.
-- It includes:
-- INSERT
-- UPDATE
-- DELETE


-- =========================================================
--                    INSERT
-- =========================================================

-- INSERT is used
-- to add new row(s)
-- into a table.

-- Syntax

/*
INSERT INTO table_name(column1, column2)
VALUES(value1, value2);
*/


-- =========================================================
--        INSERT WITHOUT IDENTITY_INSERT
-- =========================================================

-- brand_id is an IDENTITY column.

-- SQL Server automatically
-- generates the ID.

INSERT INTO production.brands (brand_name)
VALUES ('Honda');


-- =========================================================
--          INSERT WITH IDENTITY_INSERT
-- =========================================================

-- By default, SQL Server
-- does not allow inserting
-- a value into an IDENTITY column.

-- Example:

INSERT INTO production.brands (brand_id, brand_name)
VALUES (100, 'Yamaha');

-- Error:
-- Cannot insert explicit value
-- for identity column when
-- IDENTITY_INSERT is OFF.


-- Enable IDENTITY_INSERT

SET IDENTITY_INSERT production.brands ON;

-- Now we can insert
-- our own ID value.

INSERT INTO production.brands (brand_id, brand_name)
VALUES (100, 'Yamaha');

-- Disable it again

SET IDENTITY_INSERT production.brands OFF;


-- =========================================================
--             OUTPUT INSERTED
-- =========================================================

-- OUTPUT INSERTED returns
-- the newly inserted values.

INSERT INTO production.brands (brand_name)
OUTPUT INSERTED.brand_id
VALUES ('Suzuki');

-- Example Result:
--
-- brand_id
-- --------
-- 101


-- Return multiple columns

INSERT INTO production.brands (brand_name)
OUTPUT
	INSERTED.brand_id,
	INSERTED.brand_name
VALUES ('Kawasaki');


-- =========================================================
--                  SELECT
-- =========================================================

SELECT *
FROM production.brands;


-- =========================================================
--             INSERT INTO ... SELECT
-- =========================================================

-- Create a new table

CREATE TABLE production.ny_customers
(
	customer_id INT IDENTITY PRIMARY KEY,
	customer_name VARCHAR(100)
);

-- We can insert data
-- from another table
-- using a SELECT query.

-- VALUES keyword is not used
-- with INSERT ... SELECT.

INSERT INTO production.ny_customers (customer_name)
SELECT
	CONCAT(first_name, ' ', last_name)
FROM sales.customers
WHERE state = 'NY';

SELECT *
FROM production.ny_customers;


-- =========================================================
--                    UPDATE
-- =========================================================

-- UPDATE is used
-- to modify existing data.

SELECT *
FROM production.brands;

UPDATE production.brands
SET brand_name = 'DELL'
WHERE brand_name = 'New Brand';


-- =========================================================
--                   GETDATE()
-- =========================================================

-- GETDATE() returns
-- the current date and time.

-- It is commonly used
-- for created_at
-- and updated_at columns.

SELECT GETDATE();