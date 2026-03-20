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

def generate_insights(data):
    """
    Analyzes the data and returns 3 meaningful conclusions as strings.
    """
    if not data:
        return ["No data available."]

    insights = []

    # Insight 1: Highest Rated Entry (Most Popular)
    # Find the dictionary with the highest rating value
    best_item = max(data, key=lambda x: float(x['rating']))
    insights.append(f"Quality Leader: '{best_item['title']}' is the highest-rated entry in the dataset with a score of {best_item['rating']}.")

    # Insight 2: Value Threshold (Finacial Success)
    # Counting how many items exceeded a specific 'value' 
    threshold = 100
    high_value_count = len([r for r in data if float(r['value']) > threshold])
    insights.append(f"Commercial Success: {high_value_count} entries have exceeded a value of {threshold}, showing strong market performance.")

    # Insight 3: Era Analysis (Retro vs. Modern)
    # Count to see if the dataset favors older or newer entries
    modern_count = len([r for r in data if int(r['year']) >= 2015])
    if modern_count > (len(data) / 2):
        insights.append(f"Trend: The dataset is majority 'Modern' (released 2015 or later), suggesting a focus on current trends.")
    else:
        insights.append(f"Trend: The dataset features a significant number of 'Retro' entries, providing a historical perspective.")

    return insights
# ============================================================



# ============================================================
# Part 7 : export_report(data, output_filepath, top_n=5)

def export_report(data, output_filepath, top_n=5):
    """
    Writes a formatted data analysis report to a text file.
    
    Parameters:
    data (list): A list of dictionaries representing the dataset.
    output_filepath (str): The path where the .txt report will be saved.
    top_n (int): The number of top-rated entries to include (default is 5).
    """

    # Get the overall summary metrics
    summary = summarize(data)
    
    sorted_data = sorted(data, key=lambda x: float(x['rating']), reverse=True)
    top_entries = sorted_data[:top_n]
    
    with open(output_filepath, mode='w', encoding='utf-8') as report_file:
        report_file.write("========================================\n")
        report_file.write("       PROJECT 1: ANALYSIS REPORT       \n")
        report_file.write("========================================\n\n")
        
        # Overall Summary
        report_file.write("--- OVERALL SUMMARY ---\n")
        report_file.write(f"Total Records: {summary['total_records']}\n")
        report_file.write(f"Unique Genres: {summary['unique_genres']}\n")
        report_file.write(f"Average Rating: {summary['average_rating']}\n\n")
        
        # Top Rated Entries
        report_file.write(f"--- TOP {top_n} RATED ENTRIES ---\n")
        for entry in top_entries:
            report_file.write(f"- {entry['title']} ({entry['year']}) | Rating: {entry['rating']}\n")
        
        report_file.write("\n--- GENERATED INSIGHTS ---\n")
        report_file.write("The dataset has been successfully processed and exported.\n")
        report_file.write("========================================\n")
# ============================================================



# ============================================================
# Part 8 : main()

def main():
    """
    Ties the program together.
    """

    filename = 'videogames.csv' 

    print(f"--- Starting Analysis for {filename} ---")

    dataset = load_data(filename)
    
    display_summary(dataset)
    
    # Exports final report as a text file 
    output_file = filename.replace('.csv', '_report.txt')
    export_report(dataset, output_file)
    
    print(f"Done! Analysis saved to {output_file}")

if __name__ == "__main__":
    main()
# ============================================================
