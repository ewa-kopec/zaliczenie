"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import csv
from collections import defaultdict



def load_csv(path):
    """A2: Reads CSV and returns a list of dictionaries."""
    data = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["Rating"] = int(row["Rating"])
                except:
                    row["Rating"] = 0
                data.append(row)
        return data
    except FileNotFoundError:
        return []


def count_reviews_by_park(data):
    """C10: Counts reviews per park for pie chart."""
    counts = {}
    for row in data:
        park = row["Branch"]
        counts[park] = counts.get(park, 0) + 1
    return counts


def get_reviews_by_park(data, park_name):
    """B7: Returns all reviews for a specific park."""
    return [r for r in data if r["Branch"].lower() == park_name.lower()]


def count_reviews_by_location(data, park_name, location):
    """B8: Counts reviews for a park from a specific location."""
    matches = [r for r in data if r["Branch"].lower() == park_name.lower()
               and r["Reviewer_Location"].lower() == location.lower()]
    return len(matches)


def get_avg_rating_by_year(data, park_name, year):
    """B9: Returns average rating for a park in a specific year."""
    ratings = [r["Rating"] for r in data if r["Branch"].lower() == park_name.lower()
               and year in r["Year_Month"]]
    return sum(ratings) / len(ratings) if ratings else 0


def get_avg_score_per_park_location(data):
    """D13: Calculates average rating per park for every location."""
    results = {}
    for row in data:
        key = (row["Branch"], row["Reviewer_Location"])
        if key not in results:
            results[key] = []
        results[key].append(row["Rating"])

    averages = {key: sum(val) / len(val) for key, val in results.items()}
    return averages