-- =========================================================
--                 CREATE DATABASE
-- =========================================================

-- Used to create a new database
CREATE DATABASE BikeStore;



-- =========================================================
--                 SELECT / FETCH DATA
-- =========================================================

/*
SELECT statement is used to fetch/get data from a table.

Syntax:

SELECT column_name
FROM table_name;

(*) is used when we want all columns from a table.
*/

-- Fetch all data from customers table
SELECT * FROM sales.customers;

-- Fetch all data from products table
SELECT * FROM production.products;

-- Fetch only specific columns
SELECT product_id, product_name
FROM production.products;

-- Fetch all data from orders table
SELECT * FROM sales.orders;

-- Fetch customer whose ID is 90
SELECT *
FROM sales.customers
WHERE customer_id = 90;

-- Fetch only first_name and last_name
SELECT first_name, last_name
FROM sales.customers;



-- =========================================================
--                 ORDER BY (SORTING)
-- =========================================================

/*
ORDER BY is used to sort the result.

ASC  -> Ascending Order
        (A-Z, 0-9, Small to Large)

DESC -> Descending Order
        (Z-A, 9-0, Large to Small)

Syntax:

SELECT column_name
FROM table_name
ORDER BY column_name ASC | DESC;
*/

-- Sort first_name from A-Z
SELECT first_name
FROM sales.customers
ORDER BY first_name;

-- Sort first_name from Z-A
SELECT first_name
FROM sales.customers
ORDER BY first_name DESC;



-- =========================================================
--        ORDER BY WITH MULTIPLE COLUMNS
-- =========================================================

/*
We can sort data using multiple columns.

First SQL sorts by the first column,
then inside that result it sorts by the second column.
*/

-- Sort by city first, then by first_name
SELECT city, first_name, last_name
FROM sales.customers
ORDER BY city, first_name;

-- city in ascending and first_name in descending
SELECT city, first_name, last_name
FROM sales.customers
ORDER BY city ASC, first_name DESC;



-- =========================================================
--                 PRACTICE OF ORDER BY
-- =========================================================

-- Sort products from low price to high price
SELECT *
FROM production.products
ORDER BY list_price ASC;

-- Sort model_year ascending
-- and list_price from high to low
SELECT *
FROM production.products
ORDER BY model_year ASC, list_price DESC;

-- Latest orders first
-- and required_date in ascending order
SELECT *
FROM sales.orders
ORDER BY order_date DESC, required_date ASC;



-- =========================================================
--            ORDER BY WITH WHERE CLAUSE
-- =========================================================

/*
WHERE clause is used for filtering data.

We can use WHERE and ORDER BY together.
First filtering happens,
then sorting is applied.
*/

SELECT city, first_name, last_name
FROM sales.customers
WHERE state = 'NY'
ORDER BY city;



-- =========================================================
--                 LIMITING ROWS
-- =========================================================

/*
Sometimes we only need limited rows.

TOP is used in SQL Server for this purpose.
*/

-- Fetch top 10 rows
SELECT TOP 10 *
FROM production.products;

-- Fetch top 10 cheapest products
SELECT TOP 10 product_id, product_name, list_price
FROM production.products
ORDER BY list_price;



-- =========================================================
--                 TOP PERCENT
-- =========================================================

/*
TOP PERCENT returns a percentage of rows, from the total rows of a table.

Formula:

(Total Rows * Percentage) / 100

Example:

If a table has 321 rows
and we use TOP 1 PERCENT:

(321 * 1) / 100
= 3.21

SQL will round the value
and return around 4 rows.
*/

SELECT *
FROM production.products;

SELECT TOP 1 PERCENT *
FROM production.products
ORDER BY list_price;



-- =========================================================
--                 OFFSET AND FETCH
-- =========================================================

/*
OFFSET:
Skips specific number of rows.

FETCH:
Returns limited rows after OFFSET.

Mostly used in pagination.
(Like Page 1, Page 2 in websites)
*/

-- Skip first 10 rows
SELECT *
FROM production.products
ORDER BY list_price
OFFSET 10 ROWS;

-- Skip first 2 rows
-- then fetch next 5 rows
SELECT *
FROM production.products
ORDER BY list_price
OFFSET 2 ROWS
FETCH NEXT 5 ROWS ONLY;



-- =========================================================
--                 NULL VALUES
-- =========================================================

/*
NULL means value does not exist.

IS NOT NULL:
Returns only rows where value exists.
*/

SELECT *
FROM sales.customers
WHERE phone IS NOT NULL;



-- =========================================================
--                 DISTINCT
-- =========================================================

/*
DISTINCT returns unique values.

Duplicate values are removed from the result.
*/

-- Fetch unique cities
SELECT DISTINCT city
FROM sales.customers
ORDER BY city;

-- Fetch unique states
SELECT DISTINCT state
FROM sales.customers
ORDER BY state;

-- Fetch unique city-state pairs
SELECT DISTINCT city, state
FROM sales.customers
ORDER BY city;

-- Fetch unique phone numbers
SELECT DISTINCT phone
FROM sales.customers
ORDER BY phone;



-- =========================================================
--                 LOGICAL OPERATORS
-- =========================================================

/*
AND:
All conditions must be TRUE.

OR:
If one condition is TRUE,
result will be returned.
*/

-- category_id = 1
-- AND list_price > 400
SELECT *
FROM production.products
WHERE category_id = 1
AND list_price > 400;

-- category_id = 1
-- OR list_price > 400
SELECT *
FROM production.products
WHERE category_id = 1
OR list_price > 400;

-- brand_id 1 or 2
-- AND list_price > 1000
SELECT *
FROM production.products
WHERE (brand_id = 1 OR brand_id = 2)
AND list_price > 1000;