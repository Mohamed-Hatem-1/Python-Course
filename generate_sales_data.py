import pandas as pd
import random

# Create a list of products
products = ["Computers", "Laptops", "Phones", "TVs", "iPads"]

# Create a list of regions
regions = ["North America", "Middle East", "Asia", "Europe"]

# Generate random sales data for multiple months
data = []

for _ in range(100):  # You can adjust the number of rows as needed
    product = random.choice(products)
    region = random.choice(regions)
    sales = random.randint(100, 1000)
    month = random.randint(1, 12)
    year = random.randint(2010, 2022)
    
    data.append([product, region, month, year, sales])

# Create a DataFrame
columns = ["Product", "Region", "Month", "Year", "Sales"]
df = pd.DataFrame(data, columns=columns)

# Save the dataset to a CSV file
df.to_csv('sales_data.csv', index=False)
