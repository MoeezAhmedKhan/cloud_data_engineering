-- =========================================================
--                 INDEXES
-- =========================================================

-- Indexes are special data structures
-- that help speed up data retrieval.

-- SQL Server provides two main types:
-- 1. Clustered Index
-- 2. Non Clustered Index


-- =========================================================
--            HOW DATA IS STORED?
-- =========================================================

-- Data is stored on disk inside pages.

-- Database have unit 'Page' and 1 Page can be stored data upto 8kb

-- See how data stores in this table:
-- Diagram Link:
-- https://excalidraw.com/#json=TbjhuMqWZslhQ9eS5ulTG,Jh3XMLk9ZdcpkuALXUriYQ


-- =========================================================
--             CLUSTERED INDEX
-- =========================================================

-- Clustered Index stores data
-- in sorted order.

-- It follows a B-Tree structure.

-- By default SQL Server creates
-- a Clustered Index on the
-- Primary Key if no Clustered Index
-- already exists.

-- Only one Clustered Index
-- can exist in a table because
-- data can have only one physical order.

-- Clustered Index is not limited
-- to the Primary Key.

-- It can be created on any column.


-- =========================================================
--                    HEAP
-- =========================================================

-- Heap is a table without
-- a Clustered Index.

-- Rows are stored
-- in no particular order.

-- =========================================================
--                   B-TREE
-- =========================================================

-- B-Tree is a balanced tree structure
-- used by SQL Server indexes.

-- It consists of:
-- Root Node
-- Intermediate Nodes
-- Leaf Nodes

-- B-Tree helps SQL Server
-- find data quickly
-- without scanning the entire table.


-- =========================================================
--             NON CLUSTERED INDEX
-- =========================================================

-- Non Clustered Index also follows
-- a B-Tree structure.

-- Leaf nodes store index keys
-- and pointers to the actual data.


-- =========================================================
--             Note
-- =========================================================


-- A table can have only one Clustered Index.

-- A table can have multiple
-- Non Clustered Indexes.

-- Clustered Index makes searching fast
-- on one column.

-- Non Clustered Indexes make searching fast
-- on other columns as well.


/*
Example Non Cluster Index:

Clustered Index = customer_id
Non Clustered Index = email

Query:

SELECT *
FROM customers
WHERE email = 'ahmed@gmail.com';

Step 1:
SQL searches email in the
Non Clustered Index B-Tree.

Step 2:
SQL navigates through:
-> Root Node
-> Intermediate Node
-> Leaf Node

Step 3:
Leaf Node contains:

Index Key:
ahmed@gmail.com

Pointer:
customer_id = 3 

Step 4:
SQL uses customer_id = 3
to search in the
Clustered Index B-Tree.

Step 5:
Clustered Index navigates through:
Root Node
-> Intermediate Node
-> Leaf Node

Step 6:
SQL reaches the actual data page.

Step 7:
Required row is returned.

Summary:

Non Clustered Index
finds where the data is.

Clustered Index
returns the actual data.
*/


-- Implementation:

CREATE TABLE production.parts
(
	part_id INT NOT NULL,
	part_name VARCHAR(255)
);

INSERT INTO 
	production.parts (part_id, part_name) 
VALUES 
	(1, 'Frame'),
	(2, 'Head light'),
	(3, 'Back light'),
	(4, 'Meter'),
	(5, 'Break'),
	(6, 'Kick')

--The production.parts table has no primary key, so SQL Server stores its data as a heap (unordered rows).

SELECT * FROM production.parts WHERE part_id = 3

-- Now check estimated execution plan it shows whole table is scanned for filter a single row.

-- Create a Primary Key.
-- SQL Server will automatically create
-- a Clustered Index if none exists.

ALTER TABLE production.parts 
ADD PRIMARY KEY (part_id);

-- Create explicit cluster index
CREATE CLUSTERED INDEX ci_part_id ON production.parts(part_id) 
-- It will show error because one cluster index already exist through primary key

-- Examples 1:

SELECT * FROM sales.orders WHERE order_id = 3

-- We are searching by customer_id
-- but the existing index is on order_id.

-- SQL Server cannot efficiently use
-- the order_id index for this query.

-- Therefore, creating a Non Clustered Index
-- on customer_id can improve performance.

SELECT * FROM sales.orders WHERE customer_id = 1212

CREATE NONCLUSTERED INDEX nci_part_id ON sales.orders(customer_id) 

-- This results in two B-Tree traversals:
-- 1. Non Clustered Index Seek
-- 2. Clustered Index Key Lookup
SELECT * FROM sales.orders WHERE customer_id = 1212


-- Example 2:

SELECT * FROM production.parts;
-- Insert large data into this table

DROP TABLE production.parts;
CREATE TABLE production.parts
(
	part_id INT IDENTITY PRIMARY KEY NOT NULL,
	part_name VARCHAR(255)
);

-- Now insert data

WITH Numbers AS
(
	SELECT TOP (100000) -- No of rows which is inserted
	ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
	FROM sys.all_objects a
	CROSS JOIN sys.all_objects b
)

INSERT INTO production.parts (part_name)
SELECT 'Part ' + CAST(n AS VARCHAR(10)) FROM Numbers;

SELECT * FROM production.parts;















-- =========================================================
--        WHY DO WE NEED CLUSTERED INDEX?
-- =========================================================

/*
Question:

If a Non Clustered Index can directly find
the Page Number and Row Number
in a Heap table, then why do we need
a Clustered Index?

Answer:

Example:

Heap Table (No Clustered Index)

part_id | part_name
--------|-----------
1       | Frame
2       | Head Light
3       | Back Light
4       | Meter

Non Clustered Index on part_id:

Root Node
    ↓
Intermediate Node
    ↓
Leaf Node

Leaf Node:

Index Key = 3
Pointer = Page 15, Row 1

SQL Query:

SELECT *
FROM production.parts
WHERE part_id = 3;

Execution:

Step 1:
SQL searches value 3
in the Non Clustered Index B-Tree.

Step 2:
SQL reaches the Leaf Node.

Step 3:
Leaf Node returns:

Index Key = 3
Pointer = Page 15, Row 1

Step 4:
SQL directly jumps to:

Page 15
Row 1

Step 5:
Required row is returned.

So why Clustered Index?

Because Heap tables become fragmented
when data is inserted, updated or deleted.

Example:

Page 1 -> part_id = 1
Page 20 -> part_id = 2
Page 5 -> part_id = 3
Page 50 -> part_id = 4

Data is scattered across pages.

For single row searches,
Non Clustered Index works well.

But for:

WHERE part_id BETWEEN 1 AND 1000

ORDER BY part_id

Large scans

Clustered Index performs much better
because data is physically stored
in sorted order.

Summary:

Heap + Non Clustered Index
= Fast lookup for individual rows.

Clustered Index
= Fast lookup, better sorting,
better range searches,
and better performance on large tables.
*/


/*
Question:

If a table has an IDENTITY column
and values are generated in sequence
(1, 2, 3, 4, ...),

then why is a Clustered Index needed?

Won't the data already be stored
in sorted order?
*/

-- Answer:

-- IDENTITY generates sequential values.

-- It does not physically sort data.

-- Heap tables may reuse empty space
-- created by deleted rows.

-- Therefore, rows may not be stored
-- in key order physically.

-- Only a Clustered Index guarantees
-- physical data ordering.