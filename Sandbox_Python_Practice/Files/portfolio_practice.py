# Portfolio practice using sample grades
# Jonathan Lee

import csv
import statistics

def calculate_statistics(data):
    #Calculate mean, median and standard deviation of a list of numbers.
    if data:  # Ensure the data list is not empty
        mean_val = statistics.mean(data)
        median_val = statistics.median(data)
        std_dev_val = statistics.stdev(data) if len(data) > 1 else 0  # Standard deviation requires at least two data points
        return mean_val, median_val, std_dev_val
    return None, None, None  # Return None if no data

def process_csv(filename):
    #Process a CSV file and calculate statistics for fall and spring semesters.
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        fall_scores = []
        spring_scores = []
        
        for row in reader:
            name, semester, score = row
            score = float(score)
            
            if 'Fall' in semester:
                fall_scores.append(score)
            elif 'Spring' in semester:
                spring_scores.append(score)
        
        fall_stats = calculate_statistics(fall_scores)
        spring_stats = calculate_statistics(spring_scores)
        
        return fall_stats, spring_stats

# Read the CSV file and calculate statistics
filename = 'Sandbox_Python_Practice\Files\sample_grades.csv'  
fall_stats, spring_stats = process_csv(filename)

# Output the results
print(f"Fall Semester: Mean = {fall_stats[0]}, Median = {fall_stats[1]}, Standard Deviation = {fall_stats[2]}")
print(f"Spring Semester: Mean = {spring_stats[0]}, Median = {spring_stats[1]}, Standard Deviation = {spring_stats[2]}")
