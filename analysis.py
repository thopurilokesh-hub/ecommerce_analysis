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
print(f"Total revenue is :{total_revenue}")
#monthly sales trend
df["Month"]=df["OrderDate"].dt.month
monthly_analysis=df.groupby("Month")["Total_Sales"].sum()
#print(f"Monthly Analysis :{monthly_analysis}")
### Best selling products
product_sales=df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(f"Best selling products:{product_sales}")