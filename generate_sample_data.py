"""
Generate sample e-commerce data for the dashboard
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define data parameters
n_records = 5000

# Define categories
categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Sports', 'Books', 'Beauty', 'Toys']
brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE', 'BrandF', 'BrandG', 'BrandH']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Cash on Delivery', 'UPI']
sellers = ['Seller1', 'Seller2', 'Seller3', 'Seller4', 'Seller5', 'Seller6', 'Seller7', 'Seller8']

# Generate customer IDs (500 unique customers)
n_customers = 500
customer_ids = [f'CUST{str(i).zfill(4)}' for i in range(1, n_customers + 1)]

# Generate data
data = []

start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

for i in range(n_records):
    # Random date
    days_diff = (end_date - start_date).days
    random_days = random.randint(0, days_diff)
    order_date = start_date + timedelta(days=random_days)
    
    # Random category and related fields
    category = random.choice(categories)
    brand = random.choice(brands)
    seller = random.choice(sellers)
    product = f'{category}_Product_{random.randint(1, 50)}'
    
    # Random customer
    customer_id = random.choice(customer_ids)
    
    # Random city
    city = random.choice(cities)
    
    # Random payment method
    payment_method = random.choice(payment_methods)
    
    # Generate sales metrics
    units_sold = random.randint(1, 10)
    unit_price = round(random.uniform(10, 500), 2)
    gross_sales = round(units_sold * unit_price, 2)
    discount = round(gross_sales * random.uniform(0, 0.3), 2)
    net_sales = round(gross_sales - discount, 2)
    cost = round(net_sales * random.uniform(0.5, 0.8), 2)
    profit = round(net_sales - cost, 2)
    
    data.append({
        'Order_ID': f'ORD{str(i+1).zfill(6)}',
        'Order_Date': order_date,
        'Year': order_date.year,
        'Month': order_date.strftime('%B'),
        'Month_Num': order_date.month,
        'Customer_ID': customer_id,
        'City': city,
        'Category': category,
        'Brand': brand,
        'Product': product,
        'Seller': seller,
        'Payment_Method': payment_method,
        'Units_Sold': units_sold,
        'Unit_Price': unit_price,
        'Gross_Sales': gross_sales,
        'Discount': discount,
        'Net_Sales': net_sales,
        'Cost': cost,
        'Profit': profit
    })

# Create DataFrame
df = pd.DataFrame(data)

# Sort by date
df = df.sort_values('Order_Date').reset_index(drop=True)

# Save to CSV
df.to_csv('ecommerce_sales_data.csv', index=False)

print(f"Generated {len(df)} records")
print(f"Date range: {df['Order_Date'].min()} to {df['Order_Date'].max()}")
print(f"Unique customers: {df['Customer_ID'].nunique()}")
print(f"Total revenue: ${df['Net_Sales'].sum():,.2f}")
print(f"Total profit: ${df['Profit'].sum():,.2f}")
print("\nData preview:")
print(df.head())
print("\nData saved to 'ecommerce_sales_data.csv'")
