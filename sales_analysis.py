import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# 1. LOAD AND INSPECT DATA
# ----------------------------------------

# Loading the dataset
data = pd.read_csv("advertising.csv")

print("First 5 rows of the dataset:")
print(data.head())

print("\nColumn Data Types:")
print(data.dtypes)

print("\nMissing Values:")
print(data.isnull().sum())

# ----------------------------------------
# 2. DATA CLEANING
# ----------------------------------------

# Converting only specific columns to numeric
cols_to_convert = ["TV", "Radio", "Newspaper", "Sales"]
data[cols_to_convert] = data[cols_to_convert].apply(pd.to_numeric)

# Dropping any missing values just in case
data = data.dropna()

# Creating new required columns
data["Units_Sold"] = data["Sales"]        # treating 'Sales' as Units sold
data["Unit_Price"] = 10                   # assuming fixed price
data["Revenue"] = data["Units_Sold"] * data["Unit_Price"]

# Adding week numbers
data["Week"] = range(1, len(data) + 1)

# Adding product column
data["Product"] = "Product A"

print("\nAfter Cleaning:")
print(data.head())

# ----------------------------------------
# 3. DESCRIPTIVE STATISTICS
# ----------------------------------------

# a. Total revenue per product
total_revenue = data.groupby("Product")["Revenue"].sum()
print("\nTotal Revenue Per Product:")
print(total_revenue)

# b. Average units sold per product
avg_units = data.groupby("Product")["Units_Sold"].mean()
print("\nAverage Units Sold Per Product:")
print(avg_units)

# c. Week with highest sales
best_week = data.loc[data["Units_Sold"].idxmax(), "Week"]
print("\nWeek with the Highest Units Sold:")
print(best_week)

# ----------------------------------------
# 4. DATA VISUALIZATION
# ----------------------------------------

# a. Line plot for units sold
plt.plot(data["Week"], data["Units_Sold"], marker='o', color='blue')
plt.title("Units Sold Over Weeks")
plt.xlabel("Week")
plt.ylabel("Units Sold")
plt.grid(True)
plt.show()

# b. Bar chart for revenue
plt.bar(total_revenue.index, total_revenue.values, color='orange')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# c. Scatter plot for marketing spend vs units sold
data["Marketing_Spend"] = data["TV"] + data["Radio"] + data["Newspaper"]

plt.scatter(data["Marketing_Spend"], data["Units_Sold"], color='green')
plt.title("Marketing Spend vs Units Sold")
plt.xlabel("Marketing Spend")
plt.ylabel("Units Sold")
plt.grid(True)
plt.show()

# ----------------------------------------
# 5. DATA ANALYSIS
# ----------------------------------------

# a. Correlation
correlation = data["Marketing_Spend"].corr(data["Units_Sold"])
print("\nCorrelation between Marketing Spend and Units Sold:")
print(round(correlation, 2))

# b. Sales growth (first week to last week)
sales_growth = data["Units_Sold"].iloc[-1] - data["Units_Sold"].iloc[0]
print("\nSales Growth from Week 1 to Last Week:")
print(sales_growth)

# c. Insights
print("\nInsights:")
print("1. Marketing spend has a positive relationship with units sold.")
print("2. Revenue depends directly on units sold since price is constant.")
print("3. There is noticeable sales growth across the weeks.")
