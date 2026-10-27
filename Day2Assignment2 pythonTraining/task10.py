import plotly.express as px

stocks = px.data.stocks()

fig = px.line(
    stocks,
    x="date",
    y=["GOOG", "AAPL", "AMZN"],
    title="Stock Prices: GOOG, AAPL, and AMZN"
)

fig.update_xaxes(rangeslider_visible=True)
fig.show()

# Use the range slider to inspect any three-month period.
# The assignment identifies AAPL as having the highest growth