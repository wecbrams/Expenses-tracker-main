-- Create the NOBEL_WIN table if it does not exist
CREATE TABLE IF NOT EXISTS NOBEL_WIN (
  YEAR INTEGER,
  SUBJECT TEXT,
  WINNER TEXT,
  COUNTRY TEXT,
  CATEGORY TEXT
);

-- Insert sample data into the NOBEL_WIN table
INSERT INTO NOBEL_WIN (YEAR, SUBJECT, WINNER, COUNTRY, CATEGORY) VALUES
  (1970, 'PHYSICS', 'HANNES ALFVEN', 'SWEDEN', 'SCIENTIST'),
  (1970, 'PHYSICS', 'LOUIS NEEL', 'FRANCE', 'SCIENTIST'),
  (1971, 'PHYSICS', 'PAUL', 'FRANCE', 'SCIENTIST'),
  (1971, 'CHEMISTRY', 'HAMILTON', 'SWEDEN', 'LINGUIST'),
  (1972, 'LITERATURE', 'BERNARD KELSON', 'GERMANY', 'ECONOMIST'),
  (1972, 'ECONOMICS', 'JOSEPH', 'RUSSIA', 'ECONOMIST'),
  (1973, 'BIOLOGY', 'PHILIPS', 'USA', 'PRIME MINISTER'),
  (1980, 'BIOLOGY', 'MARTIN', 'USA', 'PRESIDENT'),
  (1981, 'PHYSIOLOGY', 'HANNAH', 'HUNGARY', 'SCIENTIST'),
  (1975, 'PHYSICS', 'PETER', 'CHILE', 'SCIENTIST');

  SELECT * FROM NOBEL_WIN;

   SELECT * FROM NOBEL_WIN
   WHERE SUBJECT NOT LIKE 'P%';

--Create the DEPARTMENT table if it does not exist
CREATE TABLE IF NOT EXISTS DEPARTMENT (
  EMPLOYEE_ID TEXT,
  NAME TEXT,
  DEPARTMENT_ID TEXT,
  MANAGER_ID TEXT,
  SALARY REAL
);

-- Insert sample data into the DEPARTMENT table
INSERT INTO DEPARTMENT (EMPLOYEE_ID, NAME, DEPARTMENT_ID, MANAGER_ID, SALARY) VALUES
  ('100', 'STEVEN KING', '90', '100', 24000),
  ('101', 'NEENA KOCCHAR', '90', '100', 17000),
  ('102', 'LEX DEHAAN', '90', '102', 9000),
  ('103', 'BRUCE LEE', '60', '103', 4800),
  ('104', 'DIANA WILLS', '60', '103', 25000),
  ('105', 'VALLI PATOR', '50', '100', 4200),
  ('1973', 'LUV HAMI', '60', '102', 5000),
  ('106', 'DAVID AUSTIN', '90', '100', 6000);

-- Query to count the number of employees in each department
SELECT department_id AS "Department Code", 
COUNT(*) AS "No of Employees" 
FROM DEPARTMENT
GROUP BY department_id; 

-- Query to sum the salary of each department
SELECT department_id, SUM(salary) 
FROM DEPARTMENT 
GROUP BY department_id;

-- Query to count the number of employees and sum the salary in each department
SELECT department_id AS "Department Code", 
COUNT(*) AS "No of Employees", 
SUM(salary) AS "Total Salary" 
FROM DEPARTMENT 
GROUP BY department_id; 

-- Query to sum the salary of employees with a specific manager
SELECT department_id AS "Department Code", 
SUM(salary) AS "Total Salary" 
FROM DEPARTMENT 
WHERE MANAGER_ID = '103' 
GROUP BY department_id;

-- Query to find departments with more than 2 employees
SELECT department_id, COUNT(*) AS "No. of Employees" 
FROM DEPARTMENT 
GROUP BY department_id 
HAVING COUNT(*) > 2;
