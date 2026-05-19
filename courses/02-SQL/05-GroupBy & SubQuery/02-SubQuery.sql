-- =========================================
-- Sub Queries
-- =========================================

-- Sub Query:
-- A query written inside another query is called a subquery.
-- Inner query runs first, then outer query uses its result.


-- =========================================
-- Example 1
-- Get those customers' orders whose city is 'New York'
-- =========================================

-- First see customer ids from New York

SELECT 
	customer_id 
FROM 
	sales.customers 
WHERE 
	city = 'New York';


-- Without Sub Query

SELECT 
	* 
FROM 
	sales.orders 
WHERE 
	customer_id IN (16,178,327,411,854,927,1016);


-- With Sub Query (Better Approach)

SELECT 
	* 
FROM 
	sales.orders 
WHERE 
	customer_id IN (
		SELECT 
			customer_id 
		FROM 
			sales.customers 
		WHERE 
			city = 'New York'
);


-- =========================================
-- Example 2
-- Get products whose price is greater than average price
-- =========================================

SELECT 
	* 
FROM 
	production.products 
WHERE 
	list_price > (
		SELECT 
			AVG(list_price) 
		FROM 
			production.products
);


-- =========================================
-- Same Scenario With CROSS JOIN
-- Get products whose price is greater than average price
-- =========================================

SELECT
	p1.product_id,
	p1.product_name,
	p1.list_price
FROM
	production.products p1
CROSS JOIN
	production.products p2
GROUP BY
	p1.product_id,
	p1.product_name,
	p1.list_price
HAVING
	p1.list_price > AVG(p2.list_price);


-- =========================================
-- Example 3
-- Get products whose price is greater than
-- average price of Electra and Trek brands
-- =========================================

SELECT 
	product_name,
	list_price 
FROM 
	production.products 
WHERE 
	list_price > (
		SELECT 
			AVG(list_price) 
		FROM 
			production.products 
		WHERE 
			brand_id IN (
				SELECT 
					brand_id 
				FROM 
					production.brands 
				WHERE 
					brand_name IN ('Electra', 'Trek')
			)
);


-- =========================================
-- Example 4
-- Get product names of these categories:
-- Comfort Bicycles, Electric Bikes
-- =========================================

SELECT 
	* 
FROM 
	production.products 
WHERE 
	category_id IN (
		SELECT 
			category_id 
		FROM 
			production.categories 
		WHERE 
			category_name IN ('Comfort Bicycles', 'Electric Bikes')
);


-- =========================================
-- Example 5
-- Get product details where stock quantity
-- is greater than 25
-- =========================================

SELECT 
	* 
FROM 
	production.products 
WHERE 
	product_id IN (
		SELECT 
			product_id 
		FROM 
			production.stocks 
		WHERE 
			quantity > 25
);