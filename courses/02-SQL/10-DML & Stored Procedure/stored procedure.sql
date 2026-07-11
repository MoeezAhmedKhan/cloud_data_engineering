-- =========================================================
--              STORED PROCEDURES
-- =========================================================

-- A Stored Procedure is
-- a group of one or more SQL queries
-- stored in the database.

-- It can be executed
-- whenever needed.


-- =========================================================
--                 SYNTAX
-- =========================================================

/*
CREATE PROCEDURE procedure_name
AS
BEGIN
    SQL Queries
END
*/


-- =========================================================
--          CREATE SIMPLE PROCEDURE
-- =========================================================

CREATE PROCEDURE product_list
AS
BEGIN
	SELECT
		product_name,
		list_price
	FROM production.products
	ORDER BY product_name;
END


-- Execute Stored Procedure

EXEC product_list;


-- =========================================================
--      STORED PROCEDURE WITH PARAMETER
-- =========================================================

-- Parameters allow us
-- to pass values
-- into a Stored Procedure.

GO

CREATE PROCEDURE product_list2
	@min_list_price DECIMAL
AS
BEGIN
	SELECT
		product_name,
		list_price
	FROM production.products
	WHERE list_price >= @min_list_price
	ORDER BY product_name;
END


-- Execute Procedure

EXEC product_list2 2500;


-- =========================================================
--     MULTIPLE PARAMETERS & DEFAULT VALUES
-- =========================================================

GO

CREATE PROCEDURE product_list3
	@min_list_price DECIMAL = 0,
	@max_list_price DECIMAL = 500000
AS
BEGIN
	SELECT
		product_name,
		list_price
	FROM production.products
	WHERE list_price >= @min_list_price
	AND list_price <= @max_list_price
	ORDER BY product_name;
END


-- Execute Procedure

EXEC product_list3 3500, 4000;


-- Delete Stored Procedure

DROP PROCEDURE product_list3;


-- =========================================================
--                  PRACTICE QUESTION
-- =========================================================

-- Create a Stored Procedure
-- to return product name
-- and list price.

-- Return only those products
-- whose name starts with 'Trek'.

GO

CREATE PROCEDURE get_product_detail
	@search VARCHAR(255)
AS
BEGIN

	SELECT
		product_name,
		list_price
	FROM production.products
	WHERE product_name LIKE @search + '%';

END


EXEC get_product_detail
	@search = 'Trek';


DROP PROCEDURE get_product_detail;



-- =========================================================
--                  VARIABLES
-- =========================================================

-- Variables are used
-- to store temporary values.


-- Declare Variable

DECLARE @price DECIMAL;


-- Declare and Assign Value

DECLARE @brand_name VARCHAR(100) = 'Honda';


-- Set Value

DECLARE @product_price DECIMAL;

SET @product_price = 2500;


-- Print Variable

PRINT @brand_name;

SELECT @product_price;



-- =========================================================
--                  IF ELSE
-- =========================================================

-- IF ELSE is used
-- to execute different
-- blocks of code
-- based on a condition.


DECLARE @newprice DECIMAL = 3000;

IF @newprice > 2000
BEGIN
	PRINT 'Expensive Product';
END
ELSE
BEGIN
	PRINT 'Cheap Product';
END;



-- =========================================================
--                  WHILE LOOP
-- =========================================================

-- WHILE repeats
-- a block of code
-- until the condition
-- becomes FALSE.


DECLARE @count INT = 1;

WHILE @count <= 5
BEGIN

	PRINT @count;

	SET @count = @count + 1;

END;



-- =========================================================
--                  BREAK
-- =========================================================

-- BREAK immediately
-- exits the loop.


DECLARE @number INT = 1;

WHILE @number <= 10
BEGIN

	IF @number = 6
	BEGIN
		BREAK;
	END

	PRINT @number;

	SET @number = @number + 1;

END;