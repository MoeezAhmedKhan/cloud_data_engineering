USE BikeStore;


-- =========================================================
--                 CTE
-- =========================================================

/*
CTE stands for:
Common Table Expression

CTE stores temporary result.

It improves:
1. Readability
2. Reusability
*/


-- =========================================================
--                 CTE SYNTAX
-- =========================================================

/*
WITH cte_name(column_names)
AS
(
    cte_query
)
sql_statement;
*/



-- =========================================================
--                 SIMPLE CTE
-- =========================================================

/*
Get customer full names
using CTE.
*/

WITH getCustomerNames
AS
(
	SELECT
		CONCAT(first_name, ' ', last_name) full_name
	FROM
		sales.customers
)

SELECT
	*
FROM
	getCustomerNames;



-- =========================================================
--              CTE WITH COLUMN NAME
-- =========================================================

/*
-- Column names in a CTE will be the names selected in the query,
-- and these column names can be used in the SQL statements of that CTE.
*/

WITH getCustomerNames(customer_full_name)
AS
(
	SELECT
		CONCAT(first_name, ' ', last_name) full_name
	FROM
		sales.customers
)

SELECT customer_full_name FROM getCustomerNames; -- sql statement of cte



-- =========================================================
--                 CTE PRACTICE
-- =========================================================

/*
Get total sales
by each staff
according to year.
*/

WITH cte_get_sales_by_staff_of_each_year
(
	staff_id,
	staff_name,
	order_year,
	net_sale
)
AS
(
	SELECT
		s.staff_id,
		CONCAT(first_name, ' ', last_name) full_name,
		YEAR(o.order_date) order_year,
		SUM(oi.quantity * oi.list_price * (1 - oi.discount)) net_sale
	FROM
		sales.staffs s
	INNER JOIN
		sales.orders o
	ON
		s.staff_id = o.staff_id
	INNER JOIN
		sales.order_items oi
	ON
		oi.order_id = o.order_id
	GROUP BY
		s.staff_id,
		CONCAT(first_name, ' ', last_name),
		YEAR(o.order_date)
)

SELECT
	*
FROM
	cte_get_sales_by_staff_of_each_year
WHERE
	order_year = '2016';



-- =========================================================
--               CTE + AVG
-- =========================================================

/*
Get average order count
of all staffs.
*/

WITH findOrderCountByStaffId
(
	staff_id,
	order_count
)
AS
(
	SELECT
		staff_id,
		COUNT(*) AS order_count
	FROM
		sales.orders
	GROUP BY
		staff_id
)

SELECT
	AVG(order_count) AS avg_order_count
FROM
	findOrderCountByStaffId;



-- =========================================================
--                    NOTE
-- =========================================================

/*
Any column used in SELECT
without Aggregate Function
must also be used
in GROUP BY.
*/



-- =========================================================
--             PRODUCT COUNT BY CATEGORY
-- =========================================================

/*
Get:
category_id,
category_name
and total products.
*/

SELECT
	p.category_id,
	c.category_name,
	COUNT(product_id) product_count
FROM
	production.categories c
INNER JOIN
	production.products p
ON
	p.category_id = c.category_id
GROUP BY
	p.category_id,
	c.category_name;



-- =========================================================
--              CATEGORY WISE SALE
-- =========================================================

/*
Get category wise
total net sale.
*/

SELECT
	p.category_id,
	c.category_name,
	SUM(oi.quantity * oi.list_price * (1 - oi.discount)) net_sale
FROM
	production.categories c
INNER JOIN
	production.products p
ON
	p.category_id = c.category_id
INNER JOIN
	sales.order_items oi
ON
	oi.product_id = p.product_id
GROUP BY
	p.category_id,
	c.category_name;


-- Now convert both queries into cte and make join of both cte and output will be 
-- (category_id, category_name, product_count, net_sale)

-- =========================================================
--                MULTIPLE CTE
-- =========================================================

/*
Get:
category_id,
category_name,
product_count
and net_sale
using multiple CTEs.
*/

WITH cte_product_count_by_category
AS
(
	SELECT
		p.category_id,
		c.category_name,
		COUNT(product_id) product_count
	FROM
		production.categories c
	INNER JOIN
		production.products p
	ON
		p.category_id = c.category_id
	GROUP BY
		p.category_id,
		c.category_name
),

cte_category_wise_sale
AS
(
	SELECT
		p.category_id,
		c.category_name,
		SUM(oi.quantity * oi.list_price * (1 - oi.discount)) net_sale
	FROM
		production.categories c
	INNER JOIN
		production.products p
	ON
		p.category_id = c.category_id
	INNER JOIN
		sales.order_items oi
	ON
		oi.product_id = p.product_id
	GROUP BY
		p.category_id,
		c.category_name
)

SELECT
	c.category_id,
	c.category_name,
	product_count,
	net_sale
FROM
	cte_product_count_by_category c
INNER JOIN
	cte_category_wise_sale s
ON
	s.category_id = c.category_id;



-- =========================================================
--             MULTIPLE CTE PRACTICE
-- =========================================================

/*
Get product net sale of completed orders:

category_id,
category_name,
product_count,
net_sale,
and order_status.

Show only completed orders
(order_status = 4).
*/

WITH cte_product_count_by_category
AS
(
	SELECT
		p.category_id,
		c.category_name,
		COUNT(product_id) product_count
	FROM
		production.categories c
	INNER JOIN
		production.products p
	ON
		p.category_id = c.category_id
	GROUP BY
		p.category_id,
		c.category_name
),

cte_category_wise_sale
AS
(
	SELECT
		p.category_id,
		c.category_name,
		SUM(oi.quantity * oi.list_price * (1 - oi.discount)) net_sale,
		o.order_status
	FROM
		production.categories c
	INNER JOIN
		production.products p
	ON
		p.category_id = c.category_id
	INNER JOIN
		sales.order_items oi
	ON
		oi.product_id = p.product_id
	INNER JOIN
		sales.orders o
	ON
		o.order_id = oi.order_id
	GROUP BY
		p.category_id,
		c.category_name,
		o.order_status
)

SELECT
	c.category_id,
	c.category_name,
	product_count,
	net_sale,
	order_status
FROM
	cte_product_count_by_category c
INNER JOIN
	cte_category_wise_sale s
ON
	s.category_id = c.category_id
WHERE
	order_status = 4;