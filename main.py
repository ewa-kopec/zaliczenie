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

    # POPRAWKA: Zmiana nazwy pliku na małe litery i dodanie ścieżki do folderu 'data'
    # Jeśli plik nie jest w folderze data, usuń "data/" z poniższej linii
    dataset = process.load_csv("data/disneyland_reviews.csv")

    if not dataset:
        # Próba awaryjna, jeśli plik jest jednak w głównym folderze
        dataset = process.load_csv("disneyland_reviews.csv")

    if not dataset:
        print("Error: CSV file not found! Please check if the file is in the project folder.")
        return

    print(f"Dataset loaded. Total records: {len(dataset)}")  # A2

    while True:
        choice = tui.display_main_menu()  # A3

        if choice == "A":  # Section B
            sub = tui.display_sub_menu_a()
            if sub == "A":
                park = input("Enter Park (e.g. Disneyland_Paris): ")
                reviews = process.get_reviews_by_park(dataset, park)
                if reviews:
                    for r in reviews[:5]:
                        print(f"ID: {r['Review_ID']} | Rating: {r['Rating']}")
                else:
                    print("No reviews found for this park.")
            elif sub == "B":
                park = input("Enter Park: ")
                loc = input("Enter Location: ")
                print(f"Count: {process.count_reviews_by_location(dataset, park, loc)}")
            elif sub == "C":
                park = input("Enter Park: ")
                yr = input("Enter Year: ")
                print(f"Avg Rating: {process.get_avg_rating_by_year(dataset, park, yr):.2f}")
            elif sub == "D":  # D13
                scores = process.get_avg_score_per_park_location(dataset)
                if scores:
                    for (p, l), avg in list(scores.items())[:10]:
                        print(f"{p} | {l}: {avg:.2f}")
                else:
                    print("No scores calculated.")

        elif choice == "B":  # Section C
            sub = tui.display_sub_menu_b()
            if sub == "A":
                counts = process.count_reviews_by_park(dataset)
                visual.plot_reviews_per_park_pie(counts)
            elif sub == "B":
                # Tutaj przekazujemy realne dane zamiast przykładowych
                print("Generating Top 10 Locations Bar Chart...")
                # Pobieramy dane dla ogólnej statystyki lokalizacji
                loc_data = {}
                for r in dataset:
                    loc = r['Reviewer_Location']
                    loc_data[loc] = loc_data.get(loc, 0) + 1
                visual.plot_top10_locations_bar("All Parks", loc_data)

        elif choice == "X":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")  # A4


if __name__ == "__main__":
    run()