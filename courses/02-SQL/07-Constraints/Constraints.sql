USE BikeStore;



-- =========================================================
--                 CONSTRAINTS
-- =========================================================

/*
Constraints are rules
that control what data
can be stored in a table.
*/


-- =========================================================
--             TYPES OF CONSTRAINTS
-- =========================================================

/*
1. PRIMARY KEY
2. FOREIGN KEY
3. NOT NULL
4. UNIQUE
5. CHECK
*/



-- =========================================================
--                 PRIMARY KEY
-- =========================================================

/*
PRIMARY KEY uniquely identifies
each row.

PRIMARY KEY cannot contain NULL.
*/


-- Example:

/*
CREATE TABLE table_name
(
	id INT PRIMARY KEY
)
*/



-- =========================================================
--                 COMPOSITE KEY
-- =========================================================

/*
When multiple columns together
make a PRIMARY KEY,
it is called Composite Key.
*/


-- Example:

/*
CREATE TABLE order_item
(
	order_id INT,
	item_id INT,

	PRIMARY KEY (order_id, item_id)
)
*/



-- =========================================================
--                 ALTER TABLE
-- =========================================================

/*
ALTER is used
to modify table structure.
*/


-- Example:

/*
CREATE TABLE tbl_name
(
	order_id INT,
	item_id INT,
	quantity INT
)

ALTER TABLE tbl_name
ADD PRIMARY KEY (order_id, item_id)
*/



-- =========================================================
--                 FOREIGN KEY
-- =========================================================

/*
FOREIGN KEY creates relationship
between tables.

It also maintains
referential integrity.
*/


CREATE TABLE vendor_group
(
	group_id INT PRIMARY KEY IDENTITY,
	group_name VARCHAR(100)
);



CREATE TABLE vendors
(
	vendor_id INT PRIMARY KEY IDENTITY,
	vendor_name VARCHAR(100),
	group_id INT,

	CONSTRAINT fk_group
	FOREIGN KEY (group_id)

	REFERENCES vendor_group (group_id)

	ON DELETE SET NULL
);


-- Constraint name is optional.
-- We can directly write FOREIGN KEY.



-- =========================================================
--                 INSERT DATA
-- =========================================================

INSERT INTO vendor_group (group_name)
VALUES
	('Kabab Jees'),
	('Fauji Group'),
	('Ghani Group'),
	('Lucky Group');


SELECT * FROM vendor_group;



INSERT INTO vendors (vendor_name, group_id)
VALUES
	('Kabab Jees Bakers', 1),
	('Kabab Jees Fried Chiken', 1),
	('Kabab Jees Express', 1),
	('Askari Foods', 2),
	('Fauji Fertilizer', 2),
	('Nurpur Dairy', 2),
	('Ghani Glass', 3),
	('Ghani Dairies', 3),
	('Ghani Textiles', 3),
	('Lucky Cement', 4),
	('Lucky Motors', 4),
	('Lucky Foods', 4);


SELECT * FROM vendors;



-- =========================================================
--             REFERENTIAL INTEGRITY
-- =========================================================

/*
Referential Integrity ensures
relationships between tables
remain valid and consistent.
*/


-- =========================================================
--                 ON UPDATE
-- =========================================================

/*
ON UPDATE NO ACTION
ON UPDATE CASCADE
ON UPDATE SET NULL
ON UPDATE SET DEFAULT
*/



-- =========================================================
--                 ON DELETE
-- =========================================================

/*
ON DELETE NO ACTION
ON DELETE CASCADE
ON DELETE SET NULL
ON DELETE SET DEFAULT
*/



-- Example:

DELETE FROM vendor_group
WHERE group_id = 1;

SELECT * FROM vendors;



-- =========================================================
--                 NOT NULL
-- =========================================================

/*
NOT NULL does not allow
NULL values.
*/


DROP TABLE vendors;
DROP TABLE vendor_group;



CREATE TABLE vendor_group
(
	group_id INT PRIMARY KEY,
	group_name VARCHAR(100) NOT NULL
);



INSERT INTO vendor_group (group_name)
VALUES (1);

-- Error will occur
-- because NULL value
-- is being inserted
-- into group_id.



-- =========================================================
--                 UNIQUE
-- =========================================================

/*
UNIQUE ensures
duplicate values
cannot be inserted.
*/


-- =========================================================
--            PRIMARY KEY VS UNIQUE
-- =========================================================

/*
PRIMARY KEY:
Cannot contain NULL.

UNIQUE:
Can contain NULL
only one time.
*/


-- Example:

/*
CREATE TABLE tbl_name
(
	id INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE
)
*/



-- =========================================================
--              CREATE PERSON TABLE
-- =========================================================

/*
Apply:
PRIMARY KEY,
NOT NULL
and UNIQUE constraints.
*/

CREATE TABLE PERSON
(
	id INT PRIMARY KEY IDENTITY,
	fullname VARCHAR(100),
	cnic VARCHAR(100) NOT NULL UNIQUE,
	DOB VARCHAR(100) NOT NULL UNIQUE,
	phone VARCHAR(100) UNIQUE
);



INSERT INTO PERSON (fullname, cnic, DOB, phone)
VALUES
	('Ali', '4254111254124', '20-10-2001', '0378455478'),
	('Ahmed', '4288741254124', '18-10-2001', '0314998778'),
	('Bilal', '4254885654124', '01-10-2001', '0366555478');


SELECT * FROM PERSON;



-- =========================================================
--                 CHECK CONSTRAINT
-- =========================================================

/*
CHECK ensures
data follows
a specific condition.
*/


CREATE TABLE dummy_product
(
	id INT PRIMARY KEY IDENTITY,
	product_name VARCHAR(100) NOT NULL UNIQUE,
	unit_price INT CHECK(unit_price > 0)
);



INSERT INTO dummy_product (product_name, unit_price)
VALUES ('Mouse', 100);


INSERT INTO dummy_product (product_name, unit_price)
VALUES ('Keyboard', 0);


INSERT INTO dummy_product (product_name, unit_price)
VALUES ('LCD', 1);


SELECT * FROM dummy_product;



-- =========================================================
--                 CASE EXPRESSION
-- =========================================================

/*
CASE is used
to apply conditions
and return custom values.
*/


SELECT * FROM sales.orders;


-- order_status meanings:

/*
1 = Pending
2 = Processing
3 = Rejected
4 = Completed
*/



-- =========================================================
--                 GROUP BY STATUS
-- =========================================================

/*
Get total count
of each order status.
*/

SELECT
	order_status,
	COUNT(*) status_count
FROM
	sales.orders
GROUP BY
	order_status
ORDER BY
	order_status;



-- =========================================================
--                 CASE EXPRESSION
-- =========================================================

/*
Convert numeric order_status
into readable text.
*/

SELECT
	CASE order_status
		WHEN 1 THEN 'pending'
		WHEN 2 THEN 'processing'
		WHEN 3 THEN 'rejected'
		WHEN 4 THEN 'completed'
		ELSE 'Unknown'
	END AS order_status,

	COUNT(*) status_count

FROM
	sales.orders

GROUP BY
	order_status

ORDER BY
	order_status;



-- =========================================================
--              CASE EXPRESSION PRACTICE
-- =========================================================

/*
Get customer order value
and assign order priority.

Rules:

If order value is less than
or equal to 1000
then priority will be Low.

If order value is between
1001 and 5000
then priority will be Medium.

If order value is greater
than 5000
then priority will be High.

Also show:
customer_id,
order_id,
order_value
and order_priority.
*/


SELECT
	o.customer_id,
	o.order_id,

	SUM(oi.quantity * oi.list_price) order_value,

	CASE
		WHEN (SUM(oi.quantity * oi.list_price) <= 1000)
			THEN 'Low'

		WHEN (SUM(oi.quantity * oi.list_price)
			BETWEEN 1001 AND 5000)
			THEN 'Medium'

		WHEN (SUM(oi.quantity * oi.list_price) > 5000)
			THEN 'High'
	END AS order_priority

FROM
	sales.orders o

INNER JOIN
	sales.order_items oi
ON
	oi.order_id = o.order_id

GROUP BY
	customer_id,
	o.order_id

ORDER BY
	order_value DESC;