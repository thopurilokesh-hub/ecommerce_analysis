import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("ecommerce_data.csv")
#print(df.head())
#print(df.info())
df["OrderDate"]=pd.to_datetime(df["OrderDate"])#it is to convert string date to date as pandas cant understand date as string
#print(df.info())
#print(df)
#feature engineering it is very important
df["Total_Sales"]=df["Quantity"]*df["Price"]
#total revenue of the company 
total_revenue=df["Total_Sales"].sum()
#print(f"Total revenue is :{total_revenue}")
#monthly sales trend
df["Month"]=df["OrderDate"].dt.month
monthly_sales=df.groupby("Month")["Total_Sales"].sum()
#print(f"Monthly Analysis :{monthly_analysis}")
### Best selling products
product_sales=df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
#print(f"Best selling products:{product_sales}")
#Category_wise Revenue
category_revenue=df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
#print(f"Category revenue is:{category_revenue}")

### Customer anaylsis
top_customers=df.groupby("CustomerID")["Total_Sales"].sum().sort_values(ascending=False)
print(f"Top Customers are :{top_customers}")

monthly_sales.to_csv("monthly_sales.csv")
category_revenue.to_csv("category_revenue.csv")
print("✅ Analysis files saved")
category_revenue.plot(kind="bar")
plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.show()

