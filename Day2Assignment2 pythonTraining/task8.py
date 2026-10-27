import plotly.express as px

tips = px.data.tips()

fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    color="day",
    size="size",
    hover_data=["sex", "time"],
    title="Bill vs Tip"
)

fig.show()

# Interactive features:
# 1. Hover over points to see extra details.
# 2. Click legend entries to hide or show a day.