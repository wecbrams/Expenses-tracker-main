CREATE TABLE  students (
    id INT,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
);

INSERT INTO students(id,name,age,grade)VALUES
(01,'ALi',17, 10),
(21,'Taqif',16, 9),
(01,'Ramin',18, 9);

select * from students;


select * from students
where age>=17;

DROP TABLE students;

select name,grade
from students;

-- Sequence Querry Language (SQL)