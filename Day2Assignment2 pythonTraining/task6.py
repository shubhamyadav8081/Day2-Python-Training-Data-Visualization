import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker",
    style="time"
)

plt.title("Total Bill vs. Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.show()

# Smokers and non-smokers show broadly similar tipping patterns.