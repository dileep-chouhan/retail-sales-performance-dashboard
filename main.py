import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
num_products = 10
num_days = 365
# Generate random sales data for different products over a year
dates = pd.date_range(start='2023-01-01', periods=num_days)
products = [f'Product {i+1}' for i in range(num_products)]
data = {
    'Date': np.repeat(dates, num_products),
    'Product': np.tile(products, num_days),
    'Sales': np.random.randint(10, 100, size=num_days * num_products)
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Analysis ---
# Convert 'Date' column to datetime if necessary
df['Date'] = pd.to_datetime(df['Date'])
# Calculate total sales per product
total_sales_per_product = df.groupby('Product')['Sales'].sum()
top_selling_products = total_sales_per_product.nlargest(3) #Top 3 selling products
#Calculate daily average sales
daily_average_sales = df.groupby('Date')['Sales'].sum()
# --- 3. Visualization ---
#Top 3 selling products bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_selling_products.index, y=top_selling_products.values)
plt.title('Top 3 Selling Products')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_selling_products.png')
print("Plot saved to top_selling_products.png")
#Daily average sales line plot
plt.figure(figsize=(12,6))
sns.lineplot(x=daily_average_sales.index, y=daily_average_sales.values)
plt.title('Daily Average Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Daily Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('daily_average_sales.png')
print("Plot saved to daily_average_sales.png")
# --- 4. Output ---
print("\nTop 3 selling products:")
print(top_selling_products)