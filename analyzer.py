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
    Reads the dataset from the specified filepath and returns it as a list of dictionaries, where each dictionary represents a row of data with column names as keys

    PARAMETERS:
    - str filepath : The path to the CSV file containing the dataset

    RETURNS:
    - list of dict : A list of dictionaries representing the dataset, where each dictionary corresponds to a row of data with column names as keys
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

def filter_data(data,column_name, value):
    """
    Filters the list of dictionaries to find the matching values for column_name
    
    PARAMETERS:
    - data : creates a list of dictionaries representing the dataset
    - column_name (str) : String for the specific column header to search
    - value (str) : the value to search for inside the column
    RETURNS:
    - creates a new list containing only the dictionaries that match the defined criteria
    """
    filtered_results = []

    for row in data:

        if row[column_name] == value:
            filtered_results.append(row)
    
    return filtered_results
# ============================================================



# ============================================================
# Part 3 : get_category_stats(data, column)

def get_category_stats(data, column):
    """
    Calculates the average and maxium value for every category in the specific column.

    PARAMETERS:
    - data : creates a list of dictionaries representing the dataset
    - column (str) : The column to group everything

    RETURNS:
    - dict : stores where keys are in category names and values are annother dict containing the values.
    """
    stats = {}

    for row in data:
        category = row[column]
        current_value = float(row['value'])

        if category not in stats:
                stats[category] = {'sum': current_value, 'count': 1, 'max': current_value}
        else:
            stats[category]['sum'] += current_value
            stats[category]['count'] += 1
            if current_value . stats[category]['max']:
                stats[category]['max'] = current_value

    final_results = {}
    for category, values in stats.items():
        average_cal = values['sum'] / values['count']
        final_results[category] = {
            'average': round(average_cal, 2),
            'max': values['max']
        }

    return final_results
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
