-- =========================================================
--                 CREATE SCHEMA & TABLES
-- =========================================================

USE BikeStore;
GO

/*
GO separates SQL statements
into different batches.
*/


-- =========================================================
--                 CREATE SCHEMA
-- =========================================================

-- Create hr schema
CREATE SCHEMA hr;
GO



-- =========================================================
--                 CREATE TABLES
-- =========================================================

/*
IDENTITY creates auto increment values.
*/

CREATE TABLE hr.candidates
(
	id INT PRIMARY KEY IDENTITY,
	fullname VARCHAR(100) NOT NULL
);

CREATE TABLE hr.employees
(
	id INT PRIMARY KEY IDENTITY,
	fullname VARCHAR(100) NOT NULL
);



-- =========================================================
--                 INSERT DATA
-- =========================================================

-- Insert data into candidates table
INSERT INTO hr.candidates (fullname)
VALUES
	('Zia'),
	('Bilal'),
	('Ahad'),
	('Shahmeer');


-- Insert data into employees table
INSERT INTO hr.employees (fullname)
VALUES
	('Shahmeer'),
	('Ejlal'),
	('Mazhar'),
	('Zia');


-- View data
SELECT * FROM hr.employees;
SELECT * FROM hr.candidates;



-- =========================================================
--                 DROP TABLES
-- =========================================================

-- Delete tables
DROP TABLE hr.candidates;
DROP TABLE hr.employees;



-- =========================================================
--                 DROP SCHEMA
-- =========================================================

-- Delete schema
DROP SCHEMA hr;



-- =========================================================
--                 JOINS
-- =========================================================

/*
JOIN combines data
from multiple tables.
*/



-- =========================================================
--                 TYPES OF JOINS
-- =========================================================

/*
INNER JOIN:
Returns matching records
from both tables.

LEFT JOIN:
Returns all records
from left table
and matching records
from right table.

RIGHT JOIN:
Returns all records
from right table
and matching records
from left table.

FULL JOIN:
Returns all records
from both tables.

CROSS JOIN:
Returns all possible combinations
from both tables.

SELF JOIN:
Joins a table with itself.
*/



-- =========================================================
--                 INNER JOIN
-- =========================================================

/*
INNER JOIN returns
only matching rows.
*/


-- INNER JOIN Syntax

/*
SELECT
	*
FROM
	table_1
INNER JOIN
	table_2
ON
	table_1.column = table_2.column;
*/


SELECT
	hr.candidates.fullname
FROM
	hr.candidates
INNER JOIN
	hr.employees
ON
	hr.candidates.fullname = hr.employees.fullname;



-- =========================================================
--            INNER JOIN WITH ALIAS
-- =========================================================

/*
Alias gives short names
to tables.
*/

SELECT
	e.id AS employeeId,
	c.id AS candidateId,
	c.fullname
FROM
	hr.candidates AS c
INNER JOIN
	hr.employees AS e
ON
	c.fullname = e.fullname;



-- =========================================================
--           ALIAS WITHOUT AS KEYWORD
-- =========================================================

SELECT
	e.id employeeId,
	c.id candidateId,
	c.fullname
FROM
	hr.candidates c
INNER JOIN
	hr.employees e
ON
	c.fullname = e.fullname;



-- =========================================================
--                 INNER JOIN PRACTICE
-- =========================================================

/*
Get:
product_name,
list_price,
category_id
and category_name.
*/

SELECT
	product_name,
	list_price,
	c.category_id,
	c.category_name
FROM
	production.products p
INNER JOIN
	production.categories c
ON
	p.category_id = c.category_id
ORDER BY
	product_name DESC;



-- =========================================================
--                 INNER JOIN PRACTICE
-- =========================================================

/*
Get:
customer fullname,
order_status
and order_date.
*/

SELECT
	c.first_name + ' ' + c.last_name fullname,
	o.order_status,
	o.order_date
FROM
	sales.orders o
INNER JOIN
	sales.customers c
ON
	o.customer_id = c.customer_id;



-- =========================================================
--             MULTIPLE INNER JOINS
-- =========================================================

/*
Multiple INNER JOINs
can be used
in a single query.
*/

SELECT
	product_name,
	list_price,
	c.category_id,
	c.category_name,
	b.brand_id,
	b.brand_name
FROM
	production.products p
INNER JOIN
	production.categories c
ON
	c.category_id = p.category_id
INNER JOIN
	production.brands b
ON
	b.brand_id = p.brand_id;



-- =========================================================
--         MULTIPLE INNER JOIN PRACTICE
-- =========================================================

/*
Get:
customer fullname,
order_status,
order_date
and quantity.
*/

SELECT
	CONCAT(c.first_name, ' ', c.last_name) full_name,
	o.order_status,
	o.order_date,
	oi.quantity
FROM
	sales.customers c
INNER JOIN
	sales.orders o
ON
	c.customer_id = o.customer_id
INNER JOIN
	sales.order_items oi
ON
	oi.order_id = o.order_id;



-- =========================================================
--                 LEFT JOIN
-- =========================================================

/*
LEFT JOIN returns all rows
from left table
and matching rows
from right table.
*/


SELECT * FROM production.products;      -- 321 rows
SELECT * FROM sales.order_items;        -- 4722 rows
SELECT * FROM sales.orders;             -- 4722 rows



-- =========================================================
--                 LEFT JOIN PRACTICE
-- =========================================================

/*
Get:
product_name
and order_id.
*/

SELECT
	p.product_name,
	oi.order_id
FROM
	production.products p
LEFT JOIN
	sales.order_items oi
ON
	oi.product_id = p.product_id
ORDER BY
	oi.order_id ASC;      -- 4736 rows



/*
Get:
product_name,
order_id,
item_id
and order_date.
*/

SELECT
	p.product_name,
	oi.order_id,
	oi.item_id,
	o.order_date
FROM
	production.products p
LEFT JOIN
	sales.order_items oi
ON
	oi.product_id = p.product_id
LEFT JOIN
	sales.orders o
ON
	oi.order_id = o.order_id
ORDER BY
	o.order_date ASC;



/*
Get:
product_name
and order_id.
*/

SELECT
	p.product_name,
	oi.order_id
FROM
	production.products p
LEFT JOIN
	sales.order_items oi
ON
	oi.product_id = p.product_id
ORDER BY
	oi.order_id;



-- =========================================================
--                 RIGHT JOIN
-- =========================================================

/*
RIGHT JOIN returns all rows
from right table
and matching rows
from left table.
*/



-- =========================================================
--                 RIGHT JOIN PRACTICE
-- =========================================================

/*
Show all products
with their brand names.
*/

INSERT INTO production.brands (brand_name)
VALUES ('New Brand');

SELECT * FROM production.brands;


SELECT
	p.product_name,
	b.brand_name
FROM
	production.products p
RIGHT JOIN
	production.brands b
ON
	p.brand_id = b.brand_id
ORDER BY
	b.brand_id;



/*
Show all orders
with customer names.
*/

SELECT * FROM sales.customers;

INSERT INTO sales.customers
(
	first_name,
	last_name,
	phone,
	email,
	street,
	city,
	state,
	zip_code
)
VALUES
(
	'Ben',
	'Poindextor',
	'(123) 456-789',
	'ben@gmail.com',
	'xyz street',
	'Albany',
	'NY',
	'11000'
);


SELECT
	c.customer_id,
	c.first_name,
	c.last_name,
	o.order_date,
	o.order_id
FROM
	sales.orders o
RIGHT JOIN
	sales.customers c
ON
	o.customer_id = c.customer_id
ORDER BY
	c.customer_id DESC;



/*
Show all stocks
with store names.
*/

SELECT * FROM production.stocks;
SELECT * FROM sales.stores;


INSERT INTO sales.stores
(
	store_name,
	phone,
	email,
	street,
	city,
	state,
	zip_code
)
VALUES
(
	'Opal POS',
	'(789) 456-123',
	'opalpos@gmail.com',
	'xyz street',
	'Dallas',
	'Texas',
	'00011'
);


SELECT
	sto.store_name,
	stc.product_id,
	stc.quantity
FROM
	production.stocks stc
RIGHT JOIN
	sales.stores sto
ON
	sto.store_id = stc.store_id
ORDER BY
	stc.product_id;



-- =========================================================
--                 FULL JOIN
-- =========================================================

/*
FULL JOIN returns all rows
from both tables.

Non matching values become NULL.
*/


SELECT * FROM hr.employees;
SELECT * FROM hr.candidates;


-- INNER JOIN Result
SELECT
	c.id CandidateId,
	c.fullname CandidateName,
	e.id EmployeeId,
	e.fullname EmployeeName
FROM
	hr.candidates c
INNER JOIN
	hr.employees e
ON
	e.fullname = c.fullname;


-- LEFT JOIN Result
SELECT
	c.id CandidateId,
	c.fullname CandidateName,
	e.id EmployeeId,
	e.fullname EmployeeName
FROM
	hr.candidates c
LEFT JOIN
	hr.employees e
ON
	e.fullname = c.fullname;


-- RIGHT JOIN Result
SELECT
	c.id CandidateId,
	c.fullname CandidateName,
	e.id EmployeeId,
	e.fullname EmployeeName
FROM
	hr.candidates c
RIGHT JOIN
	hr.employees e
ON
	e.fullname = c.fullname;


-- FULL JOIN Result
SELECT
	c.id CandidateId,
	c.fullname CandidateName,
	e.id EmployeeId,
	e.fullname EmployeeName
FROM
	hr.candidates c
FULL JOIN
	hr.employees e
ON
	e.fullname = c.fullname;



-- =========================================================
--                 CROSS JOIN
-- =========================================================

/*
CROSS JOIN returns
all possible combinations.

No comparison is used.
*/

SELECT
	p.product_name,
	s.store_name
FROM
	production.products p
CROSS JOIN
	sales.stores s;



-- =========================================================
--                 SELF JOIN
-- =========================================================

/*
SELF JOIN joins
a table with itself.
*/


-- =========================================================
--                 SELF JOIN PRACTICE
-- =========================================================

/*
Get:
staff_name
and manager_name.
*/

SELECT
	e.staff_id,
	CONCAT(e.first_name, ' ', e.last_name) staff_name,
	m.staff_id,
	CONCAT(m.first_name, ' ', m.last_name) manager_name
FROM
	sales.staffs e
INNER JOIN
	sales.staffs m
ON
	e.staff_id = m.manager_id;



/*
Get customers
living in same city.
*/

SELECT
	c1.customer_id,
	CONCAT(c1.first_name, ' ', c1.last_name) customer_name_1,
	CONCAT(c2.first_name, ' ', c2.last_name) customer_name_2,
	c1.city
FROM
	sales.customers c1
INNER JOIN
	sales.customers c2
ON
	c1.customer_id > c2.customer_id
	AND c1.city = c2.city
WHERE
	c1.city = 'Albany'
ORDER BY
	city;