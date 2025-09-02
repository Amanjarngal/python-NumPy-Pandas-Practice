import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("productDetail.csv")

df["Date"] = pd.to_datetime(df["Date"],errors = "coerce")

# Total sales per product/category
df["Sales"] = df["Quantity"] * df["Price"]
sale_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
sale_category = df.groupby("Category")["Quantity"].sum().sort_values(ascending=False)
print(sale_category)
print("")
print(sale_product)

print("")

# Best-selling products (by quantity sold)
best_saler = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(best_saler)

print("")

# Sales trends (monthly)
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

print("")

# Customer segmentation by region & spending
region_sales = df.groupby("Customer Region")["Sales"].sum()
print(region_sales)