import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()
iris = px.data.iris()
stocks = px.data.stocks()
tips.head()
plt.figure(figsize=(8, 5))
sns.countplot(
    data=tips,
    x="day",
    order=["Thur", "Fri", "Sat", "Sun"],
    color="pink"
)
plt.title("Number of Customers by Day")
plt.xlabel("Day")
plt.ylabel("Number of Records")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    order=["Thur", "Fri", "Sat", "Sun"],
    color="teal"
)
plt.title("Average Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Bill ($)")
plt.show()

avg_bills = tips.groupby("day")["total_bill"].mean()
print(avg_bills)
print("Highest Average Bill Day:", avg_bills.idxmax())

# Most customers: Saturday
# Highest average bill: Sunday
