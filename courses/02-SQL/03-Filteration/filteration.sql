USE BikeStore;



-- =========================================================
--                 AND / OR
-- =========================================================

/*
AND:
All conditions must be TRUE.

OR:
If one condition is TRUE,
row will be returned.
*/

SELECT * 
FROM production.products 
WHERE list_price > 1000 AND brand_id = 1 OR brand_id = 2;

-- SQL first runs:
-- (list_price > 1000 AND brand_id = 1)

-- Then:
-- OR brand_id = 2

-- Internally SQL treats it like:
-- (list_price > 1000 AND brand_id = 1)
-- OR
-- (brand_id = 2)

-- That is why all products with brand_id = 2
-- are also returned.



-- =========================================================
--                 OR
-- =========================================================

/*
OR is used for multiple possible values.
*/

SELECT 
	* 
FROM 
	production.products 
WHERE 
	list_price = 999.99
	OR list_price = 1320.99 
	OR list_price = 3999.99
	OR list_price = 1799.99 
	OR list_price = 1549.99 
ORDER BY 
	list_price ASC;



-- =========================================================
--                 IN
-- =========================================================

/*
IN checks multiple values in the same column. It works like multiple OR conditions
but the query becomes shorter and cleaner.
*/

SELECT 
	* 
FROM 
	production.products 
WHERE 
	list_price IN (999.99, 1320.99, 3999.99, 1799.99, 1549.00)
ORDER BY 
	list_price ASC;



-- =========================================================
--                 NOT IN
-- =========================================================

/*
NOT IN returns values
except given values.
*/

SELECT 
	* 
FROM 
	production.products 
WHERE 
	list_price NOT IN (999.99, 1320.99, 3999.99, 1799.99, 1549.00)
ORDER BY 
	list_price ASC;



-- =========================================================
--                 BETWEEN
-- =========================================================

/*
BETWEEN checks values
within a range.
*/

SELECT 
	* 
FROM 
	production.products 
WHERE 
	list_price BETWEEN 379.99 AND 429.00;



-- =========================================================
--                 BETWEEN WITH DATES
-- =========================================================

/*
BETWEEN can also work with dates.
*/

SELECT 
	* 
FROM 
	sales.orders 
WHERE 
	order_date BETWEEN '2016-01-01' AND '2016-01-31'
ORDER BY 
	order_date ASC;



-- =========================================================
--                 NOT BETWEEN
-- =========================================================

/*
NOT BETWEEN checks values
outside the range.
*/

SELECT 
	* 
FROM 
	sales.orders 
WHERE 
	order_date NOT BETWEEN '2016-01-01' AND '2016-01-05'
ORDER BY 
	order_date ASC;


-- Alias
SELECT first_name + ' ' + last_name AS Fullname FROM sales.customers;

-- Like
-- Logical operator is used to check or match with specified string/text used with wildcard (%,_,^,[])

-- % Represent multiple character

SELECT * FROM sales.customers WHERE first_name LIKE 'A%' ORDER BY first_name;
SELECT * FROM sales.customers WHERE first_name LIKE '%a' ORDER BY first_name;
-- Its mean a kahin bhi ho data le kr ayga ye.
SELECT * FROM sales.customers WHERE first_name LIKE '%a%' ORDER BY first_name;

-- Single Character 2nd Letter a. _ is used to check single character
SELECT 
	customer_id, first_name, last_name 
FROM 
	sales.customers 
WHERE 
	first_name LIKE '_a%'; -- It will return only those name which 2nd character is 'a'

-- Question: Print those name which is not starting with a

SELECT 
	customer_id, first_name, last_name 
FROM 
	sales.customers 
WHERE 
	first_name NOT Like 'A%'

-- Question: Print those name which is start with T and end with d
SELECT 
	customer_id, first_name, last_name 
FROM 
	sales.customers 
WHERE 
	first_name Like 't%d'