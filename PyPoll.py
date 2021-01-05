#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter.
total_votes = 0
#Candidate Options
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}
#Track the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    #print(headers)
    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #candidate results
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's cote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #Save the findal vote count to the tet file
    for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100
            #Declare candidate results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #Print each candidate's voter count and percentage to terminal
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count, voting percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    #Print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)