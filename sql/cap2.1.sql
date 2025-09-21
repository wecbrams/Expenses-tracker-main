-- Create the nomnom table if it does not exist
CREATE TABLE IF NOT EXISTS nomnom (
  NAME TEXT,
  NEIGHBOURHOOD TEXT,
  CUISINE TEXT,
  REVIEW REAL,
  PRICE TEXT,
  HEALTH TEXT
);

-- Insert sample data into the nomnom table
INSERT INTO nomnom (NAME, NEIGHBOURHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
  ('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
  ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
  ('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
  ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
  ('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
  ('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
  ('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
  ('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),
  ('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

-- Select all records
SELECT * FROM nomnom;

-- Distinct NEIGHBOURHOODS and CUISINES
SELECT DISTINCT NEIGHBOURHOOD FROM nomnom;   
SELECT DISTINCT CUISINE FROM nomnom;

-- Records filtered by various criteria
SELECT * FROM nomnom WHERE CUISINE = 'Chinese';
SELECT * FROM nomnom WHERE REVIEW >= 4;
SELECT * FROM nomnom WHERE CUISINE = 'Italian' AND PRICE = '$$$';
SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';
SELECT * FROM nomnom WHERE NEIGHBOURHOOD IN ('Midtown', 'Downtown', 'Chinatown');

-- Top-rated restaurants (top 4)
SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;

-- Restaurants sorted by name alphabetically
SELECT * FROM nomnom ORDER BY NAME ASC;

-- Restaurants sorted by health grade
SELECT * FROM nomnom ORDER BY HEALTH ASC;

-- Count how many restaurants per neighborhood
SELECT NEIGHBOURHOOD, COUNT(*) AS TotalRestaurants
FROM nomnom
GROUP BY NEIGHBOURHOOD;

-- Average review score by cuisine
SELECT CUISINE, AVG(REVIEW) AS AvgReview
FROM nomnom
GROUP BY CUISINE;

-- Highest review per cuisine
SELECT CUISINE, MAX(REVIEW) AS MaxReview
FROM nomnom
GROUP BY CUISINE;

-- Restaurants with missing health grades
SELECT * FROM nomnom WHERE HEALTH IS NULL OR HEALTH = '';

-- Restaurants with cheapest price level
SELECT * FROM nomnom WHERE PRICE = '$' ORDER BY REVIEW DESC;

-- Group by PRICE and get average review
SELECT PRICE, AVG(REVIEW) AS AvgReviewByPrice
FROM nomnom
GROUP BY PRICE
ORDER BY AvgReviewByPrice DESC;

-- Count restaurants by health grade
SELECT HEALTH, COUNT(*) AS CountByHealth
FROM nomnom
GROUP BY HEALTH;

-- Add a new column (optional)
ALTER TABLE nomnom ADD COLUMN DELIVERY_AVAILABLE TEXT;

-- Update delivery option for certain rows
UPDATE nomnom SET DELIVERY_AVAILABLE = 'Yes' WHERE CUISINE = 'Pizza';
UPDATE nomnom SET DELIVERY_AVAILABLE = 'No' WHERE CUISINE !='Pizza';

-- Delete a record (example)
DELETE FROM nomnom WHERE NAME = 'Marea';

-- Change a review score manually
UPDATE nomnom SET REVIEW = 4.2 WHERE NAME = 'Jongro';

-- Search restaurants with review between 3.5 and 4.5
SELECT * FROM nomnom WHERE REVIEW BETWEEN 3.5 AND 4.5;

-- Count all restaurants
SELECT COUNT(*) AS TotalRestaurants FROM nomnom;

-- Restaurants with multi-word names
SELECT * FROM nomnom WHERE NAME LIKE '% %';

-- Restaurants with review below average
SELECT * FROM nomnom
WHERE REVIEW < (SELECT AVG(REVIEW) FROM nomnom);

-- Find duplicate cuisine entries
SELECT CUISINE, COUNT(*) AS Count
FROM nomnom
GROUP BY CUISINE
HAVING Count > 1;

-- Compare two neighborhoods’ average ratings
SELECT NEIGHBOURHOOD, AVG(REVIEW) AS AvgReview
FROM nomnom
WHERE NEIGHBOURHOOD IN ('Brooklyn', 'Midtown')
GROUP BY NEIGHBOURHOOD;

-- Find most expensive restaurants (based on price length)
SELECT *, LENGTH(PRICE) AS PriceLevel
FROM nomnom
ORDER BY LENGTH(PRICE) DESC, REVIEW DESC;

CREATE table newTable AS 
SELECT * FROM nomnom;

INSERT INTO newTable
SELECT * FROM nomnom;

Select * FROM newTable;

