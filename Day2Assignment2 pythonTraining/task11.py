import pandas as pd

comparison_data = {
    "Library": ["Matplotlib", "Seaborn", "Plotly"],
    "Ease of use": ["Medium", "Easy", "Medium"],
    "Interactive charts": ["No", "No", "Yes"],
    "Best used for": [
        "Fine-grained customization and static plots",
        "Statistical data visualization",
        "Interactive dashboards and web apps"
    ]
}

comparison_df = pd.DataFrame(comparison_data)

print("\n--- Task 11: Library Comparison Table ---")
print(comparison_df.to_string(index=False))

print("\n--- Library Recommendations ---")

print(
    "For a lab report, choose Matplotlib or Seaborn "
    "because they create clean, high-resolution static images."
)

print(
    "For a web page, choose Plotly because users can zoom, "
    "hover, and explore data interactively."
)