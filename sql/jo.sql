create table if not exists salesman(
salesman_id text primary key,
name text,
city text,
comission real);

insert into salesman(salesman_id,name,city,comission)VALUES
('5001','James bond','new york',0.15),
('5002','Neil armstrong','London',0.12),
('5003','Sam hen','Paris',0.11),
('5004','Mc lyon','London',0.14),
('5005','Laura Adam','rome',0.12),
('5006','Paul parker','new jersey',0.13);

create table if not exists customer(
customer_id text,
cust_name text primary key,
city text,
grade integer,
salesman_id text,
FOREIGN key (salesman_id) references salesman(salesman_id)
);

insert into customer (customer_id,cust_name,city,grade,salesman_id)VALUES
('3002', 'nick rimando', 'new york', 100, '5001'),

('3007', 'brad davis', 'new york', 200, '5001'),

('3005', 'graham zusi', 'california', 200, '5002'),

('3008', 'julian green', 'london', 300, '5002'),

('3004', 'fabian johnson', 'paris', 300, '5006'),

('3009', 'geoff cameron', 'berlin', 100, '5003'),

('3003', 'jozy altidor', 'moscow', 200, '5007'),

('3001', 'brad guzan', 'london', NULL, '5005');

create table if not exists orders(
ord_no text primary key,
purch_amt real,
ord_date text,
customer_id text,
salesman_id text,
FOREIGN key (customer_id) REFERENCES customer(customer_id),
FOREIGN key (salesman_id) REFERENCES salesman(salesman_id));

insert into orders(ord_no,purch_amt,ord_date,customer_id,salesman_id) VALUES
('70001', 150.5, '2012-10-05', '3005', '5002'),

('70009', 270.65, '2012-09-10', '3001', '5001'),

('70002', 65.26, '2012-10-05', '3002', '5003'),

('70004', 110.5, '2012-08-17', '3009', '5007'),

('70007', 948.5, '2012-09-10', '3005', '5005'),

('70005', 2400.6, '2012-07-27', '3007', '5006');

--queries
--matching customers with cities
select customer.cust_name,salesman.name,salesman.city
from customer
join salesman on customer.city=salesman.city;

--linking customers to their salesman
select customer.cust_name, salesman.name
from customer
join salesman on customer.salesman_id=salesman.salesman_id;

--fetching orders where customer's city does not match salesman's city
select orders.ord_no ,customer.cust_name, orders.customer_id,orders.salesman_id
from orders
join customer on orders.customer_id=customer.customer_id
join salesman on orders.salesman_id=salesman.salesman_id
where customer.city <> salesman.city;

--fetching all orders with customer names
select orders.ord_no, customer.cust_name
from orders
join customer on orders.customer_id = customer.customer_id;

--customers with grades
select customer.cust_name as 'customer', customer.grade as 'grade'
from orders
join salesman on orders.salesman_id = salesman.salesman_id
join customer on orders.customer_id=customer.customer_id
where customer.grade is not null;

--customer with salesman where commission is between 0.12 and 0.14
select customer.cust_name as 'customer',
customer.city as 'city',
salesman.name as 'salesman',
salesman.comission
from customer
join salesman on customer.salesman_id =salesman.salesman_id
where salesman.comission between 0.12 and 0.14;

--calculating comissions for orders where customer grade is 200 or more
select order.ord_no, customer.cust_name, salesman.comission as 'comissions%',
orders.purch_amt * salesman.comission as 'comission'
from orders
join salesman on orders.salesman_id=salesman.salesman_id
join customer on orders.customer_id = customer.customer_id
where customer.grade>=200;

--orders on a specific date
select *
from customer
join orders on customer.customer_id = orders.customer_id
where orders.ord_date='2012-10-05';