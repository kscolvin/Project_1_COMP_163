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
    - tuple : (min, max, average) rounded to 2 decimal places
    """
    if not data:
        return (0.0, 0.0, 0.0)
    
    values = [float(row[column]) for row in data]

    min_val = min(values)
    max_val = max(values)
    avg_val = sum(values) / len(values)

    return (round(min_val, 2), round(max_val, 2), round(avg_val, 2))
# ============================================================



# ============================================================
# Part 4 : summarize(data)

def summarize(data):
    """
    Summarizes the dataset by printing the min, max, and average 
    values for every unique genre found in the data.
    
    Parameters:
   - data : A list of dictionaries representing the dataset.
    """

    if not data:
        return {
            "total_records": 0,
            "unique_genres": 0,
            "average_rating": 0.0
        }

    total_records = len(data)

    unique_gnere_list = []
    for row in data:
        if row['genre'] not in unique_gnere_list:
            unique_gnere_list.append(row['genre'])

    num_unique_genres = len(unique_gnere_list)

    all_ratings = [float(row['rating']) for row in data]
    avg_rating = sum(all_ratings) / total_records

    summary_report = {
        "total_records": total_records,
        "unique_genres": num_unique_genres,
        "average_rating": round(avg_rating, 2)
    }

    return summary_report 
# ============================================================



# ============================================================
# Part 5 : display_summary(data)

def display_summary(data):
    """
    Prints a formatted summary of the dataset to the console.
    
    Parameters:
    data (list): A list of dictionaries representing the dataset.
    """

    report = summarize(data)

    print("================================")
    print("    DATASET ANALYSIS SUMMARY    ")
    print("================================")

    print(f"Total Number of Records: {report['total_records']}")
    print(f"Number of Unique Genres: {report['unique_genres']}")
    print(f"Average Rating: {report['average_rating']}")

    print("================================")
# ============================================================


# ============================================================
# Part 6 : generate_insights(data)


# ============================================================



# ============================================================
# Part 7 : export_report(data, output_filepath, top_n=5)

def export_report(data, output_filepath, num_entries=5):
    """
    Writes a formatted data analysis report to a text file.
    
    Parameters:
    - data : A list of dictionaries representing the dataset.
    -  output_filepath (str): The path where the .txt report will be saved.
    - top_n (int): The number of top-rated entries to include (default is 5).
    """

    summary = summarize(data)

    # Selects entries from the dataset 
    selected_entries = data[:num_entries]

    # writing out the file with the 'with' statement 
    with open(output_filepath, mode='w', encoding='utf-8') as report_file:
        report_file.write("================================\n")
        report_file.write("   PROJECT 1: ANALYSIS REPORT   \n")
        report_file.write("================================\n\n")

        # Overal Summary Code
        report_file.write("--- OVERALL SUMMARY ---\n")
        report_file.write(f"Total Records: {summary['total_records']}\n")
        report_file.write(f"Unique Genres: {summary['unique_genres']}\n")
        report_file.write(f"Average Rating: {summary['average_rating']}\n\n")

        report_file.write(f"--- FIRST {num_entries} RATED ENTRIES ---\n")
        for entry in selected_entries:
            report_file.write(f"- {entry['title']} ({entry['year']}) | Rating: {entry['rating']}\n")

        report_file.write("\n--- GENERATED INSIGHTS ---\n")
        report_file.write("The dataset has been successfully processed and exported.\n")
        report_file.write("================================\n")
# ============================================================



# ============================================================
# Part 8 : main()


# ============================================================
