import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()
iris = px.data.iris()
stocks = px.data.stocks()
tips.head()
avg_tip = tips.groupby("day")["tip"].mean().reindex(
    ["Thur", "Fri", "Sat", "Sun"]
)

print(avg_tip)

plt.figure(figsize=(8, 5))
plt.bar(avg_tip.index, avg_tip.values, color="pink")
plt.title("Average Tips by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.show()