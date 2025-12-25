import pandas as pd

df = pd.read_csv(r"C:\Users\mrkau\Desktop\customer-segemntation-analysis\data\online_retail.csv")

print("Data loaded successfully")
print(df.head())
print(df.columns)
print(df.shape)


# ================================
# 2. BASIC DATA CLEANING
# ================================

# Remove rows with missing values
df = df.dropna()

# Keep only positive quantities
df = df[df['Quantity'] > 0]

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("Data cleaning completed")


# ================================
# 3. CREATE RFM METRICS
# ================================

# Snapshot date (last date in dataset)
snapshot_date = df['InvoiceDate'].max()

# RFM calculation
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'InvoiceNo': 'count',                                     # Frequency
    'TotalPrice': 'sum'                                       # Monetary
}).reset_index()

# Rename columns
rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

print("RFM metrics created")
print(rfm.head())


# ================================
# 4. SIMPLE CUSTOMER SEGMENTATION
# ================================

rfm['Segment'] = 'Regular'

rfm.loc[rfm['Monetary'] >= rfm['Monetary'].quantile(0.75), 'Segment'] = 'High Value'
rfm.loc[rfm['Recency'] > 180, 'Segment'] = 'At Risk'

print("Customer segmentation completed")
print(rfm['Segment'].value_counts())


# ================================
# 5. SAVE OUTPUT FOR SQL
# ================================

rfm.to_csv(
    r"C:\Users\mrkau\Desktop\customer-segemntation-analysis\data\customer_rfm.csv",
    index=False
)

print("customer_rfm.csv saved successfully")
