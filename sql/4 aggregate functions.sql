create table if not exists products(
product_id Text PRimary key,
product_name TEXT,
supplier_id Text,
Category_id Text,
Unit Text,
Price REal,
name text);

INSERT INTO products(product_id,product_name, supplier_id, category_id,Unit,Price, name) VALUES
('1','chain','1' ,'1', '10 boxes* 20bags',18, 'Ali'),
('2','chang','1' ,'1', '10-24 boxes* 20bags',19, 'jouri'),
('3','Syrup','1' ,'2', '11-550 boxes* 20ml',10, 'Musa'),
('4','chef antony','2' ,'2', '40-7 JArs* 20bags',22,'Ali'),
('5','chef antony mix','2' ,'2', '40 JArs* 20bags',21.35, 'jouri');

select * from products;

select COUNT(product_id) AS PRoduct_Count
FROM products;

select AVG(Price) AS Average_Price
FROM products;

SELECT sum(Price) As TOtal_Price
FROM products;

SELECT DISTinct supplier_id from products;
SELECT DISTinct name ,supplier_id   from products;
SELECT DISTinct name ,supplier_id   from products
Where PRice>20;