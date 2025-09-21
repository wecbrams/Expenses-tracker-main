CREATE TABLE if not exists products(
pid text,
pname text,
sid text,
Cid text,
unit text,
price real 
);
INSERT INTO products(pid,pname,sid,Cid,unit,price)VALUES
('1','Watch','1','1','10 box', 18),
('2','Tv','1','1','10 box', 11),
('3','phone','2','2','20 box', 15),
('4','Lortion','3','2','11 box', 180);

SELECT count(pid) AS Product_Count
from products;

select AVG(price) AS Average_price
from products;
 
SELECT sum(price) AS TOTAL_PRICE from products;

SELECT COUNT(*) AS Expensive_Products 
FROM products 
WHERE price > 50;
