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

# Preparing total vote counter, list of candidates etc
total_votes = 0 # Total Vote Counter
candidate_options = [] # List of Candidate Name
candidate_votes = {} # Dictionary to Store No. of Votes for each Candidate

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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


# Output Results to terminal & text file
with open(file_to_save,"w") as txt_file:
    # Print Header & Total Number of Votes
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results) # To terminal
    txt_file.write(election_results) # To text file

    # Print Results for each candidate
    for candidate in candidate_votes:
        # Retrieve vote count and calculate vote percentage
        votes = candidate_votes[candidate]
        vote_percentage = votes/total_votes *100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Output to terminal & text file
        print(candidate_results) # To terminal
        txt_file.write(candidate_results) # To text file

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
    print(winning_candidate_summary) # To Terminal
    txt_file.write(winning_candidate_summary) # To text file
