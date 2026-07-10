-- COALESCE is used to get first Non Null value
SELECT COALESCE(NULL, NULL, NULL, NULL) result;
SELECT COALESCE(NULL, 123, 'Hello', 'World') result;
SELECT COALESCE(NULL, NULL, NULL, 'World') result;


-- COALESCE is also used when something is null so change null into something.
SELECT 
	CONCAT(first_name, last_name),
	email,
	COALESCE(phone, 'N/A')
FROM sales.customers;
	

-- Window Functions
-- Window Function calculates values for each row without grouping the rows

-- There are the functions:
-- 1. CUME_DIST
-- 2. DENSE_RANK
-- 3. FIRST_VALUE
-- 4. LAG
-- 5. LAST_VALUE
-- 6. LEAD
-- 7. NTILE
-- 8. PERCENT_RANK
-- 9. RANK
-- 10. ROW_NUMBER

-- 1. ROW_NUMBER: Its assign a sequential row number of each partion of set, row number start with 1 of each first row in partition.

-- Example:

--ROW_NUMBER() OVER (
--    [PARTITION BY partition_expression, ... ]
--    ORDER BY sort_expression [ASC | DESC], ...
--)

SELECT 
   first_name, 
   last_name, 
   city,
   ROW_NUMBER() OVER (
      PARTITION BY city
      ORDER BY first_name
   ) row_num
FROM 
   sales.customers
ORDER BY 
   city;

-- Without partition by

-- It just show row number on the basis of asc order

SELECT 
   ROW_NUMBER() OVER (
	ORDER BY first_name
   ) row_num,
   first_name, 
   last_name, 
   city
FROM 
   sales.customers;

-- Now Partition by with order by on same column
-- Its make partiton on if same customer name is occur

SELECT 
   ROW_NUMBER() OVER (
	PARTITION BY first_name
	ORDER BY first_name
   ) row_num,
   first_name, 
   last_name, 
   city
FROM 
   sales.customers;


-- Question use CTE with above query and find those rows which have row number is greater than 1

WITH get_customer_info (row_number, customer_id, first_name, last_name, city)
AS(
	select 
		ROW_NUMBER() OVER (
			PARTITION BY first_name
			ORDER BY first_name
		) row_num,
		customer_id, first_name, last_name, city 
	from sales.customers
) select * from get_customer_info WHERE row_number > 1;

-- Now delete duplicate rows:

WITH get_mycustomer_info (row_number, customer_id, first_name, last_name, city)
AS(
	select 
		ROW_NUMBER() OVER (
			PARTITION BY first_name
			ORDER BY first_name
		) row_num,
		customer_id, first_name, last_name, city 
	from sales.customers
)

DELETE FROM sales.customers WHERE customer_id IN (
	select customer_id from get_mycustomer_info WHERE row_number > 1
);


-- 2. Rank:
-- Rank function work on the column for ranking record and it doesnt follow sequence. It skip sequence if same rank values occur.
 
 SELECT 
	product_id,
	product_name,
	list_price,
	RANK() OVER (
		ORDER BY list_price
	) rank_by_price
 FROM production.products;

 -- Can use partition by in rank function as per need.

-- 3. Dense Rank:
-- Same as above but It follow sequence.

 SELECT 
	product_id,
	product_name,
	list_price,
	
	RANK() OVER (
		ORDER BY list_price
	) rank_by_price, -- CAN REMOVE THIS FUNCTION HERE BECAUSE IT IS EXAMPLE OF DENSE_RANK, BUT WTTH BOTH FUNCTION WE CAN COMPARE RESULT OF RANK AND DENSE_RANK

	DENSE_RANK () OVER (
		ORDER BY list_price
	) rank_by_price
 
 FROM production.products;


 -- 4. LAG:
-- LAG() returns the value
-- from the previous row.

-- It is used to compare
-- the current row with
-- the previous row.

-- Current Row  → Employee B (60000)
-- Previous Row → Employee A (50000)

-- LAG(Salary) = 50000

-- Syntax:

-- LAG(return_value ,offset [,default]) OVER (
--    [PARTITION BY partition_expression, ... ]
--    ORDER BY sort_expression [ASC | DESC], ...
--)

CREATE VIEW sales.vw_netsales_brands
AS
	SELECT 
		c.brand_name, 
		MONTH(o.order_date) month, 
		YEAR(o.order_date) year, 
		CONVERT(DEC(10, 0), SUM((i.list_price * i.quantity) * (1 - i.discount))) AS net_sales
	FROM sales.orders AS o
		INNER JOIN sales.order_items AS i ON i.order_id = o.order_id
		INNER JOIN production.products AS p ON p.product_id = i.product_id
		INNER JOIN production.brands AS c ON c.brand_id = p.brand_id
	GROUP BY c.brand_name, 
			MONTH(o.order_date), 
			YEAR(o.order_date);


WITH cte_netsales_2018 
AS
(
	SELECT 
		month, 
		SUM(net_sales) net_sales
	FROM 
		sales.vw_netsales_brands
	WHERE 
		year = 2018
	GROUP BY 
		month
)
SELECT 
	month,
	net_sales,
	LAG(net_sales,1) OVER (
		ORDER BY month
	) previous_month_sales
FROM 
	cte_netsales_2018;

-- These query is from SQL Tutorial LED Documentation


-- 5. Lead:
-- Lead return next row value

WITH cte_netsales_2018 
AS
(
	SELECT 
		month, 
		SUM(net_sales) net_sales
	FROM 
		sales.vw_netsales_brands
	WHERE 
		year = 2018
	GROUP BY 
		month
)
SELECT 
	month,
	net_sales,
	LEAD(net_sales,1) OVER (
		ORDER BY month
	) previous_month_sales
FROM 
	cte_netsales_2018;




