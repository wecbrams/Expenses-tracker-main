CREATE TABLE nomnom(
name text,
neighbourhood text,
cuisine text,
review real,
price text,
health text);
INSERT into nomnom(name,neighbourhood,cuisine,review,price,health)VALUES
 ('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
  ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
  ('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
  ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
  ('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
  ('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
  ('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
  ('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),
  ('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');
SELECT * FROM nomnom;

SELECT DISTINCT neighbourhood from nomnom;
SELECT DISTINCT cuisine from nomnom;

SELECT * from nomnom
where cuisine='chinese';

select * from nomnom 
where review >= 4;

select * from nomnom
where cuisine ='Italian' and price='$$$';

select * from nomnom where name like '%Candy%';

select * from nomnom where neighbourhood in('Midtown', 'Downtown', 'Chinatown');

select * from nomnom order by review desc limit 4;

select * from nomnom 
where health is null;

SELECT cuisine, avg(review)as 'Average review'
from nomnom
group by cuisine
order by  review;

SELECT price, count(*) as count
from nomnom
group by price
order by price;

select neighbourhood, count(*) as count
from nomnom
group by neighbourhood
order by count desc;