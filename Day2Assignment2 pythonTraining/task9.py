import plotly.express as px

tips = px.data.tips()

fig_box = px.box(
    tips,
    x="day",
    y="total_bill",
    color="sex",
    title="Total Bill by Day and Sex"
)

fig_box.show()

fig_hist = px.histogram(
    tips,
    x="total_bill",
    color="time",
    nbins=15,
    title="Total Bill Distribution by Time"
)

fig_hist.show()

# Dinner bills are generally larger than lunch bills.