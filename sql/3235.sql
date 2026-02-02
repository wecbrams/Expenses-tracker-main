CREATE TABLE nomnom(
name text,
neighbourhood text,
cuisine text,
review real,
price text,
health text
);


INSERT into nomnom(name,neighbourhood, cuisine, review,price,health)
values

  ('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
  ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
  ('Rocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
  ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
  ('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
  ('Marea', 'Chinatown', 'Chinese', 2.4, '$$', ''),
  ('Dirty Candy', 'Uptown', 'Italian', 4.2, '$$$$', 'B'),
  ('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.9, '$$$', 'A'),
  ('Golden Unicorn', 'Uptown', 'Italian', 4.0, '$$', 'A');
  
  
SELECT * FROM nomnom;
SELECT DISTINCT neighbourhood FROM nomnom;
SELECT DISTINCT CUISINE FROM nomnom;
SELECT DISTINCT cuisine from nomnom;
SELECT * FROM nomnom where cuisine="Chinese";
SELECT * FROM nomnom WHERE cuisine="Italian" and price="$$$";
SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';
SELECT * FROM nomnom WHERE neighbourhood IN ('Midtown', 'Downtown', 'Chinatown');
SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;
