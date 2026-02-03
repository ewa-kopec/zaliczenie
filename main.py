"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import process
import tui
import visual


def run():
    tui.display_header()
    dataset = process.load_csv("Disneyland_reviews.csv")

    if not dataset:
        print("Error: CSV file not found!")
        return

    print(f"Dataset loaded. Total records: {len(dataset)}")  # A2

    while True:
        choice = tui.display_main_menu()  # A3

        if choice == "A":  # Section B
            sub = tui.display_sub_menu_a()
            if sub == "A":
                park = input("Enter Park: ")
                reviews = process.get_reviews_by_park(dataset, park)
                for r in reviews[:5]: print(f"ID: {r['Review_ID']} | Rating: {r['Rating']}")
            elif sub == "B":
                park = input("Enter Park: ");
                loc = input("Enter Location: ")
                print(f"Count: {process.count_reviews_by_location(dataset, park, loc)}")
            elif sub == "C":
                park = input("Enter Park: ");
                yr = input("Enter Year: ")
                print(f"Avg Rating: {process.get_avg_rating_by_year(dataset, park, yr):.2f}")
            elif sub == "D":  # D13
                scores = process.get_avg_score_per_park_location(dataset)
                for (p, l), avg in list(scores.items())[:10]:
                    print(f"{p} | {l}: {avg:.2f}")

        elif choice == "B":  # Section C
            sub = tui.display_sub_menu_b()
            if sub == "A":
                visual.plot_reviews_per_park_pie(process.count_reviews_by_park(dataset))
            elif sub == "B":
                print("Showing sample Bar Chart...")
                visual.plot_top10_locations_bar("General", {"USA": 5, "UK": 4, "Canada": 3})

        elif choice == "X":
            print("Goodbye!");
            break
        else:
            print("Invalid option!")  # A4


if __name__ == "__main__":
    run()