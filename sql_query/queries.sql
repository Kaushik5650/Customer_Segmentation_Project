-- Total customers per segment
SELECT Segment, COUNT(*) AS NumCustomers, AVG(Monetary) AS AvgMonetary
FROM customer_rfm
GROUP BY Segment;

-- Top 10 high-value customers
SELECT CustomerID, Monetary
FROM customer_rfm
ORDER BY Monetary DESC
LIMIT 10;

-- At-risk customers (Recency > 180)
SELECT CustomerID, Recency, Segment
FROM customer_rfm
WHERE Recency > 180;
