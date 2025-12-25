# customer_rfm_sqlite.py

import sqlite3
import pandas as pd

# ================================
# 1. LOAD CLEANED DATA
# ================================
df = pd.read_csv("data/customer_rfm.csv")
print("Customer RFM data loaded successfully")
print(df.head())

# ================================
# 2. CONNECT TO SQLITE DATABASE
# ================================
conn = sqlite3.connect("sqlite_db/customer_segmentation.db")
cursor = conn.cursor()

# ================================
# 3. CREATE/REPLACE TABLE IN SQLITE
# ================================
df.to_sql("customer_rfm", conn, if_exists="replace", index=False)
print("Data saved to SQLite database successfully")

# ================================
# 4. RUN SAMPLE SQL QUERIES
# ================================

# Total customers per segment
query_segment = """
SELECT Segment, COUNT(*) AS NumCustomers, AVG(Monetary) AS AvgMonetary
FROM customer_rfm
GROUP BY Segment;
"""
result_segment = pd.read_sql(query_segment, conn)
print("\nTotal Customers per Segment:")
print(result_segment)

# Top 10 high-value customers
query_top10 = """
SELECT CustomerID, Monetary
FROM customer_rfm
ORDER BY Monetary DESC
LIMIT 10;
"""
result_top10 = pd.read_sql(query_top10, conn)
print("\nTop 10 High-Value Customers:")
print(result_top10)

# At-risk customers (Recency > 180)
query_atrisk = """
SELECT CustomerID, Recency, Segment
FROM customer_rfm
WHERE Recency > 180;
"""
result_atrisk = pd.read_sql(query_atrisk, conn)
print("\nAt-Risk Customers (Recency > 180):")
print(result_atrisk)

# ================================
# 5. CLOSE CONNECTION
# ================================
conn.close()
print("\nSQLite connection closed")
