# ============================================================

DATASET = "videogames.csv" # Change to your chosen dataset

# ============================================================

"""
COMP 163 - Introduction to Programming
Assignment: Project - Video Game Analyzer
Name: Kennedi Colvin
GitHub Username: Kscolvin
Date: 03/16/2026
Description: This program analyzes a dataset of video games, allowing users to filter and summarize the data based on various criteria. The program includes functions to load the dataset, filter the data by specific columns and values, and calculate summary statistics such as average ratings and total sales. The program is designed to be flexible and can be easily adapted to work with different datasets by changing the DATASET variable.
AI Usage: I used AI to assist with breaking down the problem into manageable steps and providing guidance on how to implement each step. 
"""
# ============================================================

# ============================================================
# Part 1 : load_data(filepath)

import csv

def load_data(filepath):
    """
    Reads the dataset from the specified filepath and returns it as a list of dictionaries, where each dictionary represents a row of data with column names as keys.

    PARAMETERS:
    - str filepath: The path to the CSV file containing the dataset.

    RETURNS:
    - list of dict: A list of dictionaries representing the dataset, where each dictionary corresponds to a row of data with column names as keys.
    """ 
    data_list = []

    with open(filepath, mode='r', encoding='utf-8') as file:

        reader = csv.DictReader(file)

        for row in reader:
            data_list.append(row)

    return data_list
# ============================================================



# ============================================================
# Part 2 : filter_data(data, column_name, value)


# ============================================================



# ============================================================
# Part 3 : get_category_stats(data, column)

# ============================================================



# ============================================================
# Part 4 : summarize(data)


# ============================================================



# ============================================================
# Part 5 : display_summary(data)


# ============================================================


# ============================================================
# Part 6 : generate_insights(data)


# ============================================================



# ============================================================
# Part 7 : export_report(data, output_filepath, top_n=5)


# ============================================================



# ============================================================
# Part 8 : main()


# ============================================================
