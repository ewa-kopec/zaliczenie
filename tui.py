"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import csv

#from typing import Iterable, Optional


ddef display_header():
    """A1: Displays the program title."""
    print("\n" + "="*45)
    print("      DISNEYLAND REVIEWS ANALYSIS SYSTEM")
    print("="*45)

def display_main_menu():
    """A3: Main menu options."""
    print("\n[MAIN MENU]")
    print("[A] View Data")
    print("[B] Visualize Data")
    print("[X] Exit")
    return input("Selection: ").upper()

def display_sub_menu_a():
    """A6: Sub-menu for View Data."""
    print("\n[VIEW DATA SUB-MENU]")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Location")
    print("[C] Average Rating by Year")
    print("[D] Average Score per Park by Location (D13)")
    return input("Selection: ").upper()

def display_sub_menu_b():
    """A6: Sub-menu for Visualization."""
    print("\n[VISUALIZATION SUB-MENU]")
    print("[A] Most Reviewed Parks (Pie Chart)")
    print("[B] Top 10 Locations by Rating (Bar Chart)")
    print("[C] Monthly Average Rating (Bar Chart)")
    return input("Selection: ").upper()