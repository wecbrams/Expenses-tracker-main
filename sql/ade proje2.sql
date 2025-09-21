CREATE TABLE if not exists nomnom(
name text,
neb text,
cuisine text,
review real,
price text,
health text
);

INSERT INTO nomnom(name,neb,cuisine,review,price,health)VALUES
('peter','Brooklyn','steak',4.4,'$$$$','A'),
('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

SELECT * FROM nomnom;

SELECT DISTINCT neb FROM nomnom;

SELECT * FROM nomnom 
where cuisine='Chinese';

SELECT * FROM nomnom
where review>=4;

SELECT * FROM nomnom
where cuisine='Italian' AND price='$$$';

SELECT * FROM nomnom
where name like '%Candy%';

SELECT * FROM nomnom
where neb in ('Midtown', 'Downtown','Chinatown');

SELECT * FROM nomnom
order by review Desc Limit 4;