CREATE TABLE salesman(
s_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
commission REAL
);

INSERT INTO salesman(s_id,name,city,commission) VALUES
('5001', 'James', 'New York', 0.15),
('5002', 'Paul','London', 0.17),
('5003','Olamide', 'Nigeria',0.10);

SELECT * FROM salesman;


CREATE TABLE students(

s_id integer PRIMARY KEY,

s_name text,

s_age integer,

ave_grade real

);

INSERT INTO students (s_id,s_name,s_age,ave_grade)

VALUES
(001, 'Jess', 12, 78.5),
(002, 'Mark', 13, 85.0),
(003, 'Lily', 12, 92.3);

SELECT * FROM students;

SELECT s_name,ave_grade from students;

SELECT * FROM students
WHERE s_age = 12;

DROP TABLE students;

CREATE TABLE students(
s_id integer PRIMARY KEY,
s_name text,
s_age integer,
ave_grade real

);

INSERT INTO students (s_id,s_name,s_age,ave_grade)

VALUES
(001, 'Jess', 12, 78.5),
(002, 'Mark', 13, 85.0),
(003, 'Lily', 12, 92.3);

SELECT * FROM students;

SELECT s_name,ave_grade from students;

DROP TABLE students;
SELECT * FROM students;
