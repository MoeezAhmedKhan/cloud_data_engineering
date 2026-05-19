-- Sub Query --
-- Sub query is a nested query

-- Get those customer's order which is related to city 'NY'

SELECT * FROM sales.orders WHERE customer_id IN ( -- Outer Query
	SELECT customer_id FROM sales.customers WHERE city = 'New York' -- Inner Query Run First
);

-- Get those product which price is greater then avg price

SELECT * FROM production.products WHERE list_price > (
	SELECT AVG(list_price) FROM production.products
);

-- Same Scenrio with Cross Join
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

-- Now Same Scenrio With Only Electra and Trek brand name

SELECT product_name, list_price FROM production.products WHERE list_price > (
	SELECT AVG(list_price) FROM production.products WHERE brand_id IN (
		SELECT brand_id FROM production.brands WHERE brand_name IN ('Electra', 'Trek')
	)
);

-- Get Product names of these 2 categories (Comfort Bicycles, Electric Bikes)

SELECT * FROM production.products WHERE category_id IN (
	SELECT category_id FROM production.categories WHERE category_name IN ('Comfort Bicycles', 'Electric Bikes')
);


