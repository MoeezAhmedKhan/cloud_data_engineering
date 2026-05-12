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