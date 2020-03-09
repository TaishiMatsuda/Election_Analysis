# Module 03 Challenge Assignment
# Retrieve the data for election results (Resources\election_results.csv) and;
#   01. Calculate the total number of votes cast
#   02. Create complete list of county
#   03. Calculate the total number of votes in each county
#   04. Calculate the percentage of votes by county
#   05. Find out the county with the largest turnout
#   06. Create complete list of candidates who received votes
#   07. Calculate the total number of votes each candidate won
#   08. Calculate the percentage of votes each candidate won
#   09. Find out the winner of the election based on popular vote

# Dependencies Used
import csv
import os
# Assigning variable to load & save file (Make sure you are at folder Election_Analysis)
file_to_load = 'Resources\election_results.csv'
file_to_save = 'Analysis\election_analysis_challenge.txt'
# Preparing variables:
total_votes = 0             # Total Vote Counter

candidate_options = []      # List of Candidate Name
candidate_votes = {}        # Dictionary to store No. of votes for each Candidate
winning_candidate = ""      # To store Name of Winning Candidate
winning_count = 0           # Winning Vote Count Tracker
winning_percentage = 0      # Winning Vote Percentage Tracker

county_options = []         # List of County
county_votes = {}           # Dictionary to store No. of votes for each county
largest_county = ""         # To store name of County with Largest Turnout
largest_county_count = 0    # Largest County Turnout Tracker


# Open the election results and read the file
with open(file_to_load,"r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader) # Reading Header
    
    # Counting Total Votes
    for row in file_reader:
        # Calculating Total Votes
        total_votes += 1

        # Making list of candidates
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Counting Votes for each Candidates
        candidate_votes[candidate_name] += 1

        # Making list of counties
        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        # Counting Votes for each County
        county_votes[county_name] += 1

# Output Results to terminal & text file
with open(file_to_save,"w") as txt_file:
    # Print Header & Total Number of Votes
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n"
    )
    print(election_results)                     # To terminal
    txt_file.write(election_results)            # To text file

    # Print Results for each county & Determine Largest County Turnout
    for county in county_votes:
        # Retrieve vote count for each county and calculate vote percentage
        votes = county_votes[county]
        vote_percentage = votes / total_votes * 100
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        # Output to terminal & text file
        print(county_results)                   # To terminal
        txt_file.write(county_results)          # To text file
        # Calculation of county with largest turnout
        if (votes > largest_county_count):
            largest_county_count = votes
            largest_county = county
    # Output to terminal & text file
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n"        
    )
    print(largest_county_summary)               # To terminal
    txt_file.write(largest_county_summary)      # To text file

    # Print Results for each candidate & Determine Winning Count/Candidate
    for candidate in candidate_votes:
        # Retrieve vote count for each candidate and calculate vote percentage
        votes = candidate_votes[candidate]
        vote_percentage = votes / total_votes * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")        
        # Output to terminal & text file
        print(candidate_results)                # To terminal
        txt_file.write(candidate_results)       # To text file
        # Calculation of Winning vote count, percentage and Determining Winning Candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    # Output to terminal & text file
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)            # To Terminal
    txt_file.write(winning_candidate_summary)   # To text file
