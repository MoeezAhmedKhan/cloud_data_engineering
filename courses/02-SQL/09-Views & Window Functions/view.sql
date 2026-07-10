-- Views
-- A SQL View is a virtual table created from the result of a SELECT query. 
-- It doesnt save data it saves query only
-- It used for security purpose also

-- Syntax
--CREATE VIEW view_name
--AS
-- SQL SELECT QUERY

CREATE VIEW production.vw_product_brand_name
AS
SELECT p.product_name, b.brand_name FROM 
	production.products p
INNER JOIN production.brands b
ON b.brand_id = p.brand_id;

SELECT * FROM production.vw_product_brand_name;


CREATE VIEW production.vw_staff_sale(staff_name, year, sale)
AS
SELECT 
	CONCAT(first_name, last_name) full_name,
	YEAR(o.order_date) y,
	SUM(oi.list_price * oi.quantity) amount
FROM sales.order_items oi
INNER JOIN sales.orders o ON o.order_id = oi.order_id
INNER JOIN sales.staffs s ON s.staff_id = o.staff_id
GROUP BY CONCAT(first_name, last_name), YEAR(o.order_date);

SELECT * FROM production.vw_staff_sale;


-- Now If you want to save data in a view so we can use 'Indexed View'.

-- Indexed view can stored data physically in the database.

-- SQL Server automatically
-- updates the Indexed View
-- whenever the underlying
-- tables are modified.

-- No manual refresh
-- or cron job is required.

GO -- GO separates SQL statements into different batches; CREATE VIEW must be the first statement in its batch.

CREATE VIEW production.vw_null_customer_phone
WITH SCHEMABINDING
AS
SELECT
	c.customer_id,
    c.first_name,
    c.phone,
	COUNT_BIG(*) AS total_rows
FROM sales.customers AS c
INNER JOIN sales.orders AS o
ON o.customer_id = c.customer_id
WHERE c.phone IS NULL
GROUP BY c.customer_id, c.first_name, c.phone;

CREATE 
	UNIQUE CLUSTERED INDEX uidx_null_cust_phone_data 
ON production.vw_null_customer_phone(customer_id)

-- Now get data from indexed view
SELECT * FROM production.vw_null_customer_phone;

