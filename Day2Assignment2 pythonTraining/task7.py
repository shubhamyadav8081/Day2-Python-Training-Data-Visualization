import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

iris = px.data.iris()

sns.pairplot(
    iris,
    hue="species",
    vars=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

plt.show()

# Petal length and petal width best separate the species.
# Setosa is the easiest species to identify.