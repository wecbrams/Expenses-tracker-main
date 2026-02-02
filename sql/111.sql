CREATE TABLE Products(
p_id text,
p_name text,
s_id text,
c_id text,
price REAL
);
INSERT into Products(p_id,p_name,s_id,c_id,price)
VALUES
('1','chais','1','10 boxes',18),
('2','chang','1','1 boxes',19),
('3','electronic','2','10 boxes',10),
('5','cosmetics','5','10 boxes',100),
('4','clothes','2','20 rolls',12.6);

select count(p_id) as 'Product Count' from Products;
select AVG(price) as 'Average Price' from Products;
select sum(price) as 'Total price' from Products;
select Distinct(s_id)as 'Unique supplier' from Products;

