import pandas as pd
import matplotlib.pyplot as plt
import json

file_path = "C:/Users/KIIT/Desktop/DATA ANALYTICS/SQL_PROJECT_2/output_files/MonthWise_CustomerCount.json"

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Check columns
print("Columns loaded:", df.columns.tolist())

# Convert 'order_month' to datetime
df['order_month'] = pd.to_datetime(df['order_month'], format='%Y-%m')

# Convert 'total_customer' to numeric
df['total_customer'] = pd.to_numeric(df['total_customer'])

# Sort by order_month
df = df.sort_values('order_month')

# Plot
plt.figure(figsize=(14, 6))
plt.plot(df['order_month'], df['total_customer'], marker='o', linestyle='-', color='blue')
plt.title('Total Customers Over Time')
plt.xlabel('Order Month')
plt.ylabel('Total Customers')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
