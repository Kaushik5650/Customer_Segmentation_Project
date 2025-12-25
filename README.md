# Customer Segmentation Dashboard 📊

This project performs customer segmentation and RFM analysis using Python, SQL (SQLite), and Power BI. It focuses on data cleaning, customer segmentation, and interactive dashboard visualization. 
The project demonstrates an end-to-end workflow from raw data to insights and dashboards.

---


## 📌 Project Author
Rama Kaushik Murugudu  
GitHub: [kaushik5650](https://github.com/kaushik5650)  
Project Repo: [Customer_Segmentation_Project](https://github.com/kaushik5650/Customer_Segmentation_Project)

---
## 📁 Dataset
The datasets used in this project can be found in the data/ folder:

- online_retail.csv – raw transaction data
- customer_rfm.csv – cleaned RFM metrics

---
## ⚙️ Tools & Technologies Used

- **Python:** pandas, NumPy, matplotlib

- **SQL**: SQLite for querying and aggregating customer data

- **Power BI**: Interactive dashboards with slicers and filters

- **IDE**: VS Code / Jupyter Notebook

- **Version Control**: Git & GitHub

---
## 🚀 Key Features
- **Data Cleaning**: Handle missing data, remove negative quantities, calculate TotalPrice

- **RFM Analysis**: Calculate Recency, Frequency, and Monetary values for each customer

- **Customer Segmentation**: Identify High Value, Regular, and At-Risk customers

- **SQL Queries**: Total customers per segment, Top 10 High-Value customers, At-Risk customers

- **Power BI Dashboard**: Interactive visuals for insights with slicers for filtering by Segment or Monetary values

- **End-to-End Workflow**: Raw dataset → Cleaned data → Python processing → SQL queries → Power BI dashboard

---

## Project Files
- `data/` → Raw and cleaned datasets (`online_retail.csv`, `customer_rfm.csv`)  
- `python_scripts/` → Python scripts for preprocessing and SQLite operations  
- `sqlite_db/` → SQLite database (`customer_segmentation.db`)   
- `screenshots/` → Visual snapshots for README and portfolio  
- `README.md` → Project documentation  

---

## SQL Queries Example
```sql
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
```
---
### How to Run
1. Clone the repository:
```bash
git clone https://github.com/kaushik5650/Customer_Segmentation_Project.git
cd Customer_Segmentation_Project
```
2. Create Python virtual environment:
```bash
python -m venv myenv
myenv\Scripts\activate      # Windows
# source myenv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```
3. Install dependencies
```
pip install pandas numpy matplotlib
```
4. Run the Python script
```
python python_scripts/customer_rfm_processing.py
python python_scripts/customer_rfm_sqlite.py
```
---
📊 Power BI Visualizations
1. Top 10 High-Value Customers
2. Average RFM Metrics by Segment
3. At-Risk Customers
4. Customer Segment Distribution
5. Segment vs Monetary Comparison
---
