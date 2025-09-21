CREATE TABLE if NOT EXISTS department(
ei text,
Name text,
Di text,
Mi text,
salary REAL);

INSERT into department(ei,name,Di, Mi, salary)VALUES
('100','Stephen', '90','100', 24000),
('101','Ali', '90','100', 17000),
('102','Neema', '50','102', 9000),
('103','Adamide', '60','103', 4000),
('104','Eniola', '50','103', 4200),
('105','Madeeha', '90','102', 6000);

SELECT di as 'Department Code', 
count(*) as 'No of employees',
Sum(salary) as 'Totala salary'
from department
GROUP BY di;

SELECT di as 'Department Code', 
Sum(salary) as 'Totala salary'
from department
where mi = '103'
GROUP BY di;

SELECT di as 'Department Code', 
count(*) as 'No of employees'
from department
GROUP BY di
having count(*)>=2;

SELECT * from department
where name not like '%a';