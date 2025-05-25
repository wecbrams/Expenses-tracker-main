CREATE TABLE supplier(
Sno TEXT PRIMARY KEY,
Sname TEXT,
Status INTEGER,
City TEXT
);

INSERT INTO supplier(Sno, Sname, status,City) VALUES
("s1","Ali",20, "Port-louis"),
("s2","Joei",20, "YES");

SELECT * FROM supplier;

SELECT * FROM supplier WHERE City="Port-louis";
