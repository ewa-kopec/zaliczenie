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


# TUI.py - Moduł interfejsu użytkownika

def display_header():
    print("\n" + "="*40)
    print("    DISNEYLAND REVIEWS ANALYSIS SYSTEM")
    print("="*40)

def display_main_menu():
    print("\n[MAIN MENU]")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    return input("Selection: ").upper()

def display_sub_menu_a():
    print("\n[VIEW DATA SUB-MENU]")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Location")
    print("[C] Average Rating by Year")
    print("[D] Average Score per Park by Location (D13)")
    return input("Selection: ").upper()

def display_sub_menu_b():
    print("\n[VISUALISE DATA SUB-MENU]")
    print("[A] Pie chart: Number of reviews per park")
    print("[B] Bar chart: Top 10 locations")
    print("[C] Bar chart: Avg rating per month")
    return input("Selection: ").upper()

def confirm_choice(selection):
    print(f"You selected option: {selection}")
