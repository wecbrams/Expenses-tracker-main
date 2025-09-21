-- Create the STUDENT table if it does not exist
-- NOT NULL is used for NAME to ensure every student record has a name
CREATE TABLE IF NOT EXISTS STUDENT (
  ROLL_NO TEXT PRIMARY KEY, 
  NAME TEXT NOT NULL,
  ADDRESS TEXT,
  PHONE TEXT,
  AGE INTEGER
);

-- Insert sample data into the STUDENT table
INSERT INTO STUDENT (ROLL_NO, NAME, ADDRESS, PHONE, AGE) VALUES
  ('1', 'RAM', 'DELHI', '*****', 18),
  ('2', 'RAMESH', 'GURGAON', '*****', 18),
  ('3', 'SUJIT', 'ROHTAK', '*****', 20),
  ('4', 'SURESH', 'DELHI', '*****', 18),
  ('5', 'AMAN', 'ROHTAK', '*****', 20),
  ('6', 'HARSH', 'GURGAON', '*****', 18);

-- Select all records from the Salesman table to verify insertion (if required)
-- SELECT * FROM Salesman;

-- Select all records from the STUDENT table to verify insertion
SELECT * FROM STUDENT;

-- Query students who are 18 years old and live in Delhi
SELECT * FROM STUDENT
WHERE AGE = 18 AND ADDRESS = 'DELHI';

-- Query students who are 18 years old and named RAM
SELECT * FROM STUDENT WHERE AGE = 18 AND NAME = 'RAM';

-- Query students named Ram or Sujit
SELECT * FROM STUDENT WHERE NAME = 'RAM' OR NAME = 'SUJIT';

-- Query students named Ram or aged 20
SELECT * FROM STUDENT WHERE NAME = 'RAM' OR AGE = 20;

-- Query students aged 18 and named Ram or Ramesh
SELECT * FROM STUDENT WHERE AGE = 18 AND (NAME = 'RAM' OR NAME = 'RAMESH');

CREATE TABLE IF NOT EXISTS PRODUCT(
  PRO_ID TEXT PRIMARY KEY,
  PRO_NAME TEXT,
  PRO_PRICE TEXT,
  PRO_COM TEXT
);
INSERT INTO PRODUCT(PRO_ID,PRO_NAME,PRO_PRICE,PRO_COM)
VALUES
  ("101","MOTHER BOARD","3200","15"),
  ("102","KEY BOARD","450","16"),
  ("103","ZIP DRIVE","250","14"),
  ("104","SPEAKER","550","16"),
  ("105","MONITOR","5000","11"),
  ("106","DVD DRIVE","900","12"),
  ("107","CD DRIVE","800","12"),
  ("108","PRINTER","2600","13"),
  ("109","REFILL CARTRIDGE","350","13"),
  ("110","MOUSE","250","12");
SELECT pro_name, pro_price
   FROM PRODUCT
   WHERE pro_price = 
    (SELECT MIN(prio_prce) FROM PRODUCT);
    
  SELECT pro_name, pro_price
   FROM PRODUCT
   WHERE pro_price = 
    (SELECT MAX(pro_price) FROM PRODUCT);    