CREATE TABLE products(
product_id text,
product_name text,
supplier_id text,
category_id text,
unit text,
price REAL);
 insert into products(product_id,product_name,supplier_id,category_id,unit,price)VALUES
 ('1','Apples','1','1','30', 90),
 ('2','Mangoes','1','1','30', 30),
 ('3','phone','1','2','320 boxes', 190),
 ('4','Laptop','2','2','30 pieces', 1090),
 ('5','Chais','2','2','30 bags', 940);

SELECT * from products;

SELECT count(product_id) as Product_Count
from products;

SELECT avg(price) as 'Average price'
from products;

select sum(price) as 'Total price'
from products;