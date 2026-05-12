-- =========================================================
-- =========================================================
--                 ADVANCED PRACTICE QUESTIONS
-- =========================================================
-- =========================================================



-- =========================================================
--                 SELECT PRACTICE
-- =========================================================

/*
1. Fetch product_name, model_year and list_price
   from products table where list_price is greater than 3000.

2. Fetch first_name, last_name and phone
   from customers table where phone is NOT NULL.

3. Fetch all orders where order_status is 4.

4. Fetch store_name, city and state
   from stores table.

5. Fetch all products where model_year = 2018.
*/

-- SOLUTION
-- 1.
SELECT product_name, model_year, list_price FROM production.products WHERE list_price > 3000;
-- 2.
SELECT first_name, last_name, phone FROM sales.customers WHERE phone IS NOT NULL;
-- 3.
SELECT * FROM sales.orders WHERE order_status = 4;
-- 4.
SELECT store_name, city, state FROM sales.stores;
-- 5.
SELECT * FROM production.products WHERE model_year = 2018;



-- =========================================================
--                 ORDER BY PRACTICE
-- =========================================================

/*
1. Sort products by list_price descending
   and model_year ascending.

2. Sort customers by state ascending
   and last_name descending.

3. Sort orders by required_date ascending
   and shipped_date descending.

4. Sort staffs by active descending
   and first_name ascending.

5. Sort products by brand_id ascending
   and list_price descending.
*/

-- SOLUTION
-- 1.
SELECT * FROM production.products ORDER BY list_price DESC, model_year ASC;
-- 2.
SELECT * FROM sales.customers ORDER BY state ASC, last_name DESC;
-- 3.
SELECT * FROM sales.orders ORDER BY required_date ASC, shipped_date DESC;
-- 4.
SELECT * FROM sales.staffs ORDER BY active DESC, first_name ASC;
-- 5.
SELECT * FROM production.products ORDER BY brand_id ASC, list_price DESC;



-- =========================================================
--                 WHERE CLAUSE PRACTICE
-- =========================================================

/*
1. Fetch products where list_price is between 1000 and 3000.

2. Fetch customers who belong to state = 'CA'
   and city = 'Los Angeles'.

3. Fetch orders where shipped_date IS NULL.

4. Fetch staffs where active = 1
   and store_id = 2.

5. Fetch products where category_id = 2
   and model_year = 2019.
*/

-- SOLUTION
-- 1.
SELECT * FROM production.products WHERE list_price >= 1000 AND list_price <= 3000;
-- 2.
SELECT * FROM sales.customers WHERE state = 'CA' AND city = 'Los Angeles';
-- 3.
SELECT * FROM sales.orders WHERE shipped_date is NULL;
-- 4.
SELECT * FROM sales.staffs WHERE active = 1 AND store_id = 2;
-- 5.
SELECT * FROM production.products WHERE category_id = 2 AND model_year = 2019;



-- =========================================================
--                 TOP PRACTICE
-- =========================================================

/*
1. Fetch top 5 most expensive products.

2. Fetch top 10 latest orders.

3. Fetch top 3 cheapest products
   from category_id = 1.

4. Fetch top 7 customers
   sorted by first_name.

5. Fetch top 15 products
   sorted by model_year descending.
*/

-- SOLUTION
-- 1.
SELECT TOP 5 * FROM production.products ORDER BY list_price DESC;
-- 2.
SELECT TOP 10 * FROM sales.orders ORDER BY order_date DESC;
-- 3.
SELECT TOP 3 * FROM production.products WHERE category_id = 1 ORDER BY list_price ASC;
-- 4.
SELECT TOP 7 * FROM sales.customers ORDER BY first_name;
-- 5.
SELECT TOP 15 * FROM production.products ORDER BY model_year DESC;



-- =========================================================
--                 OFFSET FETCH PRACTICE
-- =========================================================

/*
1. Skip first 5 expensive products
   and fetch next 5 products.

2. Skip first 10 orders
   and fetch next 10 latest orders.

3. Skip first 3 customers sorted by city
   and fetch next 7 customers.

4. Skip first 20 products
   and fetch next 10 products sorted by product_name.

5. Skip first 5 cheapest products
   and fetch next 5 expensive products.
*/

-- SOLUTION
-- 1.
SELECT * FROM production.products ORDER BY list_price DESC OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;
-- 2.
SELECT * FROM sales.orders ORDER BY order_date DESC OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
-- 3.
SELECT * FROM sales.customers ORDER BY city OFFSET 3 ROWS FETCH NEXT 7 ROWS ONLY;
-- 4.
SELECT * FROM production.products ORDER BY product_name OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;
-- 5.
SELECT * FROM production.products ORDER BY list_price OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;


-- =========================================================
--                 DISTINCT PRACTICE
-- =========================================================

/*
1. Fetch unique model_year values from products table.

2. Fetch unique order_status values from orders table.

3. Fetch unique combinations of city and state
   from customers table.

4. Fetch unique brand_id values from products table.

5. Fetch unique store_id values from staffs table.
*/

-- SOLUTION
-- 1.
SELECT DISTINCT model_year FROM production.products;
-- 2.
SELECT DISTINCT order_status FROM sales.orders;
-- 3.
SELECT DISTINCT city, state FROM sales.customers;
-- 4.
SELECT DISTINCT brand_id FROM production.products;
-- 5.
SELECT DISTINCT store_id FROM sales.staffs;


-- =========================================================
--                 LOGICAL OPERATORS PRACTICE
-- =========================================================

/*
1. Fetch products where category_id = 1
   AND list_price > 2000
   AND model_year = 2019.

2. Fetch products where brand_id = 1
   OR brand_id = 2
   OR brand_id = 3.

3. Fetch customers where state = 'CA'
   OR state = 'NY'
   AND phone IS NOT NULL.

4. Fetch staffs where active = 1
   AND (store_id = 1 OR store_id = 2).

5. Fetch products where
   (category_id = 2 OR category_id = 3)
   AND list_price > 1500
   AND model_year >= 2018.
*/

-- SOLUTION
-- 1.
SELECT * FROM production.products WHERE category_id = 1 AND list_price > 2000 AND model_year = 2019;
-- 2.
SELECT * FROM production.products WHERE brand_id = 1 OR brand_id = 2 OR brand_id = 3;
-- 3.
SELECT * FROM sales.customers where (state = 'CA' OR state = 'NY') AND phone IS NOT NULL;
-- 4.
SELECT * FROM sales.staffs WHERE active = 1 AND (store_id = 1 OR store_id = 2);
-- 5.
SELECT * FROM production.products WHERE (category_id = 2 OR category_id = 3) AND list_price > 1500 AND model_year >= 2018;