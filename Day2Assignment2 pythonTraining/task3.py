import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()
iris = px.data.iris()
stocks = px.data.stocks()
tips.head()
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(
    tips["total_bill"],
    bins=10,
    color="skyblue",
    edgecolor="black"
)
axes[0].set_title("Distribution of Total Bills")
axes[0].set_xlabel("Total Bill ($)")
axes[0].set_ylabel("Frequency")

axes[1].scatter(
    tips["total_bill"],
    tips["tip"],
    color="coral",
    alpha=0.7
)
axes[1].set_title("Total Bill vs. Tip")
axes[1].set_xlabel("Total Bill ($)")
axes[1].set_ylabel("Tip ($)")

plt.tight_layout()
plt.savefig("tips_plots.png", dpi=150)
plt.show()

# Higher bills generally tend to have higher tips.