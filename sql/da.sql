CREATE TABLE Sales(
sale_id TEXT PRIMARY KEY,
amount REAL,
salesperson_id TEXT,
sale_date TEXT,
total_revenue REAL
);

INSERT INTO SALES(sale_id, amount, salesperson_id, sale_date,total_revenue)VALUES
('1', 2000, '102', '10/20/2024',12000);
SELECT 
    salesperson_id,
    COUNT(sale_id) AS total_sales,             -- Count the number of sales per salesperson
    SUM(amount) AS total_revenue,              -- Sum the sales amount for each salesperson
    AVG(amount) AS average_sale_amount,       -- Calculate the average sale amount
    MAX(amount) AS highest_sale,              -- Find the highest sale amount
    MIN(amount) AS lowest_sale                -- Find the lowest sale amount
FROM 
    Sales
WHERE 
    sale_date BETWEEN '2023-01-01' AND '2023-02-28'  -- Filtering by date range
GROUP BY 
    salesperson_id                             -- Group by salesperson
HAVING 
    SUM(amount) > 1000                        -- Only include salespeople with total sales above 1000
ORDER BY 
    total_revenue DESC;                       -- Sort by total revenue in descending order