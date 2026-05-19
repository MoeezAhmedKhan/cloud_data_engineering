-- ============================================================
--   Assignment: GROUP BY, HAVING & SUBQUERIES
--   Database  : BikeStores
--   Topics    : GROUP BY · Aggregate Functions · HAVING
--               Subqueries · JOINs with GROUP BY
-- ============================================================


-- ============================================================
--  SECTION A — GROUP BY & AGGREGATE FUNCTIONS
-- ============================================================

-- Q1.
-- Count the total number of orders placed by each customer.
-- Show customer_id and order_count.
-- Sort by order_count descending.

SELECT customer_id, COUNT(order_id) order_count FROM sales.orders
GROUP BY customer_id
ORDER BY COUNT(order_id) DESC;


-- Q2.
-- For each store, find the total number of orders placed.
-- Show store_id and total_orders.

SELECT store_id, COUNT(order_id) total_orders FROM sales.orders
GROUP BY store_id;


-- Q3.
-- Calculate the net revenue per order.
-- Net revenue formula: SUM( quantity * list_price * (1 - discount) )
-- Show order_id and net_revenue, sorted by net_revenue descending.
-- (Hint: use sales.order_items)

SELECT 
	order_id,
	SUM(quantity * list_price * (1 - discount)) net_revenue
FROM sales.order_items 
GROUP BY order_id
ORDER BY net_revenue DESC;


-- Q4.
-- Find the average list price of products in each category.
-- Show category_id and avg_price (rounded to 2 decimal places).
-- (Hint: use ROUND())

SELECT category_id, ROUND(AVG(list_price), 2) avg_price FROM production.products
GROUP BY category_id;


-- Q5.
-- Find the total number of orders placed in each year.
-- Show order_year and total_orders, sorted by order_year.
-- (Hint: use YEAR(order_date))

SELECT YEAR(order_date) order_year, COUNT(order_id) total_orders FROM sales.orders
GROUP BY YEAR(order_date)
ORDER BY order_year ASC;


-- ============================================================
--  SECTION B — HAVING CLAUSE
-- ============================================================

-- Q6.
-- Find customers who have placed MORE than 2 orders in total.
-- Show customer_id and order_count.

SELECT customer_id, COUNT(order_id) order_count FROM sales.orders 
GROUP BY customer_id
HAVING COUNT(order_id) > 2;


-- Q7.
-- Find categories where the AVERAGE list price is greater than $1,500.
-- Show category_id and avg_price.

SELECT category_id, AVG(list_price) avg_price FROM production.products  
GROUP BY category_id
HAVING AVG(list_price) > 1500;


-- Q8.
-- Find customers who placed at least 2 orders in the year 2017.
-- Show customer_id, order_year, and order_count.

SELECT o.customer_id, COUNT(o.order_id) order_count, YEAR(o.order_date) order_year 
FROM sales.orders o
INNER JOIN sales.customers c
ON c.customer_id = o.customer_id
WHERE YEAR(o.order_date) = 2017
GROUP BY o.customer_id, YEAR(o.order_date)
HAVING COUNT(o.order_id) >= 2


-- ============================================================
--  SECTION C — SUBQUERIES
-- ============================================================

-- Q9.
-- Find all orders placed by customers who live in 'Houston'.
-- Use a subquery to get the customer_ids first.
-- Show all columns from sales.orders.

SELECT * FROM sales.orders WHERE customer_id IN (
	SELECT customer_id FROM sales.customers WHERE city = 'Houston'
);


-- Q10.
-- Find all products whose list_price is greater than the
-- AVERAGE list_price of ALL products.
-- Show product_name and list_price.

SELECT product_name, list_price FROM production.products WHERE list_price > (
	SELECT AVG(list_price) FROM production.products
);


-- Q11.
-- Find all products that belong to the category 'Mountain Bikes'
-- or 'Road Bikes'. Use a subquery on production.categories.
-- Show product_name and list_price.

SELECT product_name, list_price FROM production.products WHERE category_id IN (
	SELECT category_id FROM production.categories WHERE category_name IN ('Mountain Bikes', 'Road Bikes')
);


-- Q12.
-- Find all customers who have NEVER placed an order.
-- Show customer_id, first_name, and last_name.
-- (Hint: use NOT IN with a subquery on sales.orders)

SELECT customer_id, CONCAT(first_name, ' ', last_name) customer_name FROM sales.customers WHERE customer_id NOT IN (
	SELECT customer_id FROM sales.orders
);


-- ============================================================
--  SECTION D — JOINs WITH GROUP BY
-- ============================================================

-- Q13.
-- Find the total number of orders per city (customer's city).
-- Join sales.orders with sales.customers.
-- Show city and total_orders, sorted by total_orders descending.

SELECT 
	c.city, COUNT(o.order_id) total_orders
FROM 
	sales.orders o 
INNER JOIN 
	sales.customers c ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_orders DESC; 


-- Q14.
-- For each staff member, count how many orders they handled.
-- Join sales.orders with sales.staffs.
-- Show staff full name (first_name + ' ' + last_name) as staff_name
-- and order_count, sorted by order_count descending.

SELECT 
	 CONCAT(first_name,' ',last_name) staff_name , COUNT(o.order_id) order_count
FROM 
	sales.staffs s
INNER JOIN
	sales.orders o
ON o.staff_id = s.staff_id
GROUP BY s.staff_id, CONCAT(first_name,' ',last_name)
ORDER BY order_count DESC;


-- Q15. (BONUS — Multi-concept)
-- Find customers who have spent more than $10,000 in total.
-- Join sales.customers → sales.orders → sales.order_items.
-- Show customer full name as customer_name and total_spent.
-- Sort by total_spent descending.
-- (Hint: JOIN + GROUP BY + HAVING)

SELECT 
	CONCAT(c.first_name, ' ', c.last_name) customer_name, 
	SUM(ot.quantity * ot.list_price * (1 - ot.discount)) total_spent
FROM 
	sales.customers c
INNER JOIN
	sales.orders o
ON o.customer_id = c.customer_id
INNER JOIN 
	sales.order_items ot
ON ot.order_id = o.order_id
GROUP BY CONCAT(c.first_name, ' ', c.last_name)
HAVING  SUM(ot.quantity * ot.list_price * (1 - ot.discount)) > 10000
ORDER BY total_spent DESC;


-- ============================================================
--  END OF ASSIGNMENT
-- ============================================================