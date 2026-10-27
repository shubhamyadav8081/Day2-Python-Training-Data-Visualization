import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()

plt.figure(figsize=(9, 5))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)
plt.title("Bill Distribution by Day and Sex")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()

# Dots beyond whiskers represent outliers.
# hue="sex" compares the groups by sex.