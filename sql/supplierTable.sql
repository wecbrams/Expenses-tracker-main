CREATE TABLE supplier(
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS INTEGER,
CITY TEXT
);

INSERT INTO supplier(SNO, SNAME, STATUS, CITY) VALUES
("S1", "Damola", 20, "London"),
("S2", "Adepapo", 10, "Abuja"),
("S3", "Jessica", 12, "Budapest");

SELECT * FROM supplier;

SELECT SNO FROM supplier;

SELECT * FROM supplier
WHERE STATUS>10;

