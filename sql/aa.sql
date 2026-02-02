CREATE table nomnom(
name text,
neighbourehood text,
cuisine text,
review real,
price real,
health text
);
INSERT INTO nomnom(name, neighbourehood, cuisine, review, price, health) VALUES
('Pasta Palace', 'Downtown', 'Italian', 4.5, 15.00, 'A'),
('Sushi Central', 'Uptown', 'Japanese', 4.7, 25.00, 'A'),
('Curry Corner', 'Midtown', 'Indian', 4.2, 12.00, 'B'),
('Burger Barn', 'Suburbs', 'American', 4.0, 10.00, 'C'),
('Taco Town', 'Downtown', 'Mexican', 4.3, 8.00, 'B');

SELECT * from nomnom;

SELECT distinct neighbourehood from nomnom;
SELECT distinct cuisine from nomnom;
SELECT * from nomnom where cuisine="American";
SELECT * from nomnom where review >=4.5;
SELECT * from nomnom 
where neighbourehood='Downtown' and review>=4.3;

SELECT * from nomnom 
where neighbourehood='Downtown' or review>=4.3;

SELECT * from nomnom 
where name like '%C%';

SELECT * from nomnom 
where neighbourehood in ('Downtown','Uptown');
