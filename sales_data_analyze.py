import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data.csv')

print(data.head())

summary_stats = data.describe()
print(summary_stats)

# Find the number of unique products and sales regions
unique_products = data['Product'].nunique()
unique_regions = data['Region'].nunique()

print(unique_products)
print(unique_regions)

# Calculate total sales per product
product_sales = data.groupby('Product')['Sales'].sum().reset_index()

print(product_sales)

# Find the top-selling product
top_selling_product = product_sales.loc[product_sales['Sales'].idxmax()]

print("The top selling product is: ",top_selling_product)

# Data Visualization
# Create a bar chart to visualize total sales per product
plt.figure(figsize=(10, 6))
plt.bar(product_sales['Product'], product_sales['Sales'])
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales per Product')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(product_sales['Sales'], labels=product_sales['Product'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Sales Across Products')
plt.show()