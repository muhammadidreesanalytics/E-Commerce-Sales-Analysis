import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("../Dataset/Ecommerce_10000_Rows.csv")

# Basic Information
print(df.head())
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Records
print("\nDuplicates:", df.duplicated().sum())

# Convert Date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

# Total Orders
total_orders = df["Order_ID"].nunique()

# Total Quantity
total_quantity = df["Quantity"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Total Quantity:", total_quantity)

# Category Analysis
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Category:")
print(category_sales)

# Region Analysis
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Region:")
print(region_sales)

# Top 5 Products
top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Products:")
print(top_products)

# Profit Margin
profit_margin = (total_profit / total_sales) * 100

print("\nProfit Margin:", round(profit_margin, 2), "%")