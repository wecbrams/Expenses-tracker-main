create TABLE department(
employee_id text,
name text,
department_id text,
manager_id text,
salary REAL);
INSERT into department(employee_id,name,department_id,manager_id,salary)VALUES
('100','Joel','9','100',27000),
('101','Ali','9','100',20000),
('102','Joseph','6','102',9000),
('103','Avaneesh','5','103',8000),
('104','Zoe','9','102',2000);

select * from department;

select department_id as "department Code",
count(*) as "Number of Employees"
From department
group by department_id;

select department_id, sum(salary)
from department
group by department_id;

select department_id as "department Code",
count(*) as "Number of Employees",
Sum(salary) as "Total salary"
From department
group by department_id;

select department_id, sum(salary)
from department
group by department_id
order by name;

SELECT     department_id AS "Department Code",
    SUM(salary) AS "Total Salary"
FROM department
GROUP BY department_id
ORDER BY SUM(salary) DESC;