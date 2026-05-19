-- =========================================================
--                 GROUP BY
-- =========================================================

/*
GROUP BY is used to group
same values together.

Mostly used with Aggregate Functions:

COUNT()
SUM()
AVG()
MIN()
MAX()
*/


-- =========================================================
--                 GROUP BY BASICS
-- =========================================================

/*
This query groups same customer_id values.

Even if customer_id appears multiple times,
GROUP BY shows only unique grouped values.
*/

SELECT
	customer_id
FROM
	sales.orders
WHERE
	customer_id = 1
GROUP BY
	customer_id;



-- Group multiple customer ids

SELECT
	customer_id
FROM
	sales.orders
WHERE
	customer_id IN (1,2)
GROUP BY
	customer_id;



-- =========================================================
--            GROUP BY WITH YEAR FUNCTION
-- =========================================================

/*
Get customer_id
and order year.

Data will be grouped by:
customer_id and order year.
*/

SELECT
	customer_id,
	YEAR(order_date) ORDER_YEAR
FROM
	sales.orders
WHERE
	customer_id IN (1,2)
GROUP BY
	customer_id,
	YEAR(order_date);



-- =========================================================
--                 GROUP BY + COUNT
-- =========================================================

/*
Get total number of orders
for customers:
1, 2 and 115
according to each year.
*/

SELECT
	customer_id,
	COUNT(order_id) order_count,
	YEAR(order_date) order_year
FROM
	sales.orders
WHERE
	customer_id IN (1,2,115)
GROUP BY
	customer_id,
	YEAR(order_date);



-- =========================================================
--                 GROUP BY + COUNT
-- =========================================================

/*
Get total customers
in each city.
*/

SELECT
	city,
	COUNT(customer_id) AS customer_count_by_city
FROM
	sales.customers
GROUP BY
	city
ORDER BY
	city;



-- =========================================================
--            GROUP BY + MIN / MAX
-- =========================================================

/*
Get maximum and minimum price
of products in each category.
*/

SELECT
	category_id,
	MAX(list_price) max_price,
	MIN(list_price) min_price
FROM
	production.products
GROUP BY
	category_id;



-- =========================================================
--                 GROUP BY + SUM
-- =========================================================

/*
Get net price
according to each order_id.
*/

SELECT
	order_id,
	SUM((quantity * list_price) * (1 - discount)) AS net_price
FROM
	sales.order_items
GROUP BY
	order_id;



-- =========================================================
--                 NET PRICE FORMULA
-- =========================================================

/*
Example:

Product Price = 100$
Discount = 30% = 0.30

Formula:

100 * (1 - 0.30)
= 70

Net Price = 70$
*/



-- =========================================================
--                 HAVING CLAUSE
-- =========================================================

/*
HAVING is used to filter
aggregate results.

HAVING works with:
COUNT, SUM, AVG, MIN, MAX

WHERE filters normal columns.
HAVING filters aggregate results.
*/


-- =========================================================
--              GROUP BY + HAVING
-- =========================================================

/*
Get customers
whose total orders are greater than 1
according to each year.
*/

SELECT
	customer_id,
	COUNT(order_id) order_count,
	YEAR(order_date) order_year
FROM
	sales.orders
WHERE
	customer_id IN (1,2,115)
GROUP BY
	customer_id,
	YEAR(order_date)
HAVING
	COUNT(order_id) > 1;



-- =========================================================
--            HAVING WITH MIN / MAX
-- =========================================================

/*
Get categories where:

minimum price > 500
and
maximum price < 10000
*/

SELECT
	category_id,
	MAX(list_price) max_price,
	MIN(list_price) min_price
FROM
	production.products
GROUP BY
	category_id
HAVING
	MIN(list_price) > 500
	AND MAX(list_price) < 10000;



-- =========================================================
--              HAVING WITH AVG
-- =========================================================

/*
Get average product price
of each category
between 500 and 1000.
*/

SELECT
	category_id,
	AVG(list_price) avg_list_price
FROM
	production.products
GROUP BY
	category_id
HAVING
	AVG(list_price) BETWEEN 500 AND 1000;