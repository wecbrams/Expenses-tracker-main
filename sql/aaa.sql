CREATE TABLE IF NOT EXISTS student(
regNo text PRIMARY KEY,
name text not NULL,
age integer,
address text
);

INSERT INTO student(regNo, name, age,address)VALUES
('1', 'Ali', 17,'Mumbai'),
('2','Joe', 15, 'Lagos'),
('3', 'Jeff', 16, 'Accra'),
('4', 'Rebecca', 18,'Dodoma'),
('5','Ginger', 19, 'Accra');

SELECT * from student;

SELECT * from student
WHERE age > 17 and address ='Accra'; 

SELECT * from student
WHERE age > 17 or address ='Accra';

SELECT * from student
WHERE name like 'J%';