CREATE TABLE IF NOT EXISTS PRODUCTS(
Product_Id TEXT PRIMARY KEY,
Product_Name TEXT,
Supplier_ID TEXT,
Category_Id TEXT,
Unit text,
Price REAL
);

--Insertion--
INSERT INTO PRODUCTS (Product_Id, Product_Name, Supplier_ID, Category_Id,Unit,Price)VALUES
  
  ('1', 'CHAIS', '1', '1', '10 BOXES*20 BAGS', 18),
  ('2', 'CHANG', '1', '1', '24-12 OZ BOTTLES', 19),
  ('3', 'ANISEED SYRUP', '1', '2', '12-550 ML BOTTLES', 10),
  ('4', 'CHEF ANTON SEASONING', '2', '2', '48- 6 OZ JARS', 22),
  ('5', 'CHEF ANTON MIX', '2', '2', '36 BOXES', 21.35),
  ('6', 'Apple','1','1', '10 ', 10);
SELECT COUNT(Product_id) AS Product_Count
FROM PRODUCTS;

SELECT AVG(Price) AS avg_price
FROM PRODUCTS;

SELECT SUM(Price) AS sum_price
FROM PRODUCTS;

SELECT DISTINCT Category_Id  AS DS
FROM PRODUCTS;
