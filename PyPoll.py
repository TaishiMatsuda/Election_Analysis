#UofT Module03 - Election Analysis
## Retrieve the data for election results (Resources\election_results.csv) and;
## 01. Calculate the total number of votes cast
## 02. Create complete list of candidates who received votes
## 03. Calculate the percentage of votes each candidate won
## 04. Calculate the total number of votes each candidate won
## 05. Find out the winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assigning variable to load & save file (Make sure you are at folder Election_Analysis)
file_to_load = 'Resources\election_results.csv'
file_to_save = 'Analysis\election_analysis.txt'

# Open the election results and read the file
with open(file_to_load,"r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

# Save
with open(file_to_save,"w") as txt_file:
    # Write
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

