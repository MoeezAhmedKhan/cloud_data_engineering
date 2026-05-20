USE BikeStore;


-- =========================================================
--                 SET OPERATORS
-- =========================================================

/*
Set Operators combine results
of multiple SELECT statements.

JOIN combines columns horizontally.
Set Operators combine rows vertically.
*/


-- =========================================================
--            TYPES OF SET OPERATORS
-- =========================================================

/*
1. UNION
2. UNION ALL
3. INTERSECT
4. EXCEPT
*/



-- =========================================================
--                 UNION
-- =========================================================

/*
UNION combines results
and removes duplicate rows.
*/


SELECT
	first_name,
	last_name
FROM
	sales.staffs          -- 10 rows

UNION

SELECT
	first_name,
	last_name
FROM
	sales.customers;      -- 1446 rows


-- Result returns 1445 rows
-- because duplicate rows are removed.



-- =========================================================
--               UNION ALL
-- =========================================================

/*
UNION ALL combines results
and also returns duplicate rows.
*/

SELECT
	first_name,
	last_name
FROM
	sales.staffs

UNION ALL

SELECT
	first_name,
	last_name
FROM
	sales.customers;


-- Result returns 1456 rows



-- =========================================================
--             RULES OF SET OPERATORS
-- =========================================================

/*
Column names can be different.

Data types should be compatible.

Number of columns
must be same.
*/


SELECT
	first_name,
	last_name,
	email
FROM
	sales.staffs

UNION ALL

SELECT
	first_name,
	last_name,
	'null' AS email
FROM
	sales.customers;



-- =========================================================
--                 INTERSECT
-- =========================================================

/*
INTERSECT returns
common rows
from both queries.
*/


-- Get common cities
-- from customers and stores

SELECT
	city
FROM
	sales.customers

INTERSECT

SELECT
	city
FROM
	sales.stores;



-- =========================================================
--            INTERSECT PRACTICE
-- =========================================================

/*
Find common names
in customers and staffs.
*/

SELECT
	first_name,
	last_name
FROM
	sales.customers

INTERSECT

SELECT
	first_name,
	last_name
FROM
	sales.staffs;


-- It means no duplicate names is matching in both tables.
-- But any one table has a duplicate rows, staff tables has minimum rows, 
-- so we have checked no any reptetive column here now check on customers it will have definitely


-- =========================================================
--            FIND DUPLICATE NAMES
-- =========================================================

/*
Get duplicate customer names.
*/

SELECT
	first_name,
	last_name,
	COUNT(*) name_count
FROM
	sales.customers
GROUP BY
	first_name,
	last_name
ORDER BY
	COUNT(*) DESC;



-- Get only names
-- having duplicates

SELECT
	first_name,
	last_name,
	COUNT(*) name_count
FROM
	sales.customers
GROUP BY
	first_name,
	last_name
HAVING
	COUNT(*) > 1;



-- =========================================================
--                 EXCEPT
-- =========================================================

/*
EXCEPT returns rows
from first query
that do not exist
in second query.
*/


SELECT
	email
FROM
	sales.customers

EXCEPT

SELECT
	email
FROM
	sales.staffs;
