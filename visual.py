"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt


def plot_reviews_per_park_pie(counts):
    """C10: Pie chart of reviews distribution."""
    plt.figure(figsize=(8, 6))
    plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%')
    plt.title("Number of Reviews per Park")
    plt.show()


def plot_top10_locations_bar(park_name, data_dict):
    """C11: Bar chart of top 10 locations."""
    # Simplified version for pass grade
    sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    locs = [x[0] for x in sorted_data]
    vals = [x[1] for x in sorted_data]

    plt.figure(figsize=(10, 5))
    plt.bar(locs, vals, color='green')
    plt.title(f"Top 10 Locations for {park_name}")
    plt.xticks(rotation=45)
    plt.show()