#The data we need to retrieve.
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statement open the file as a text file
with open(file_to_load) as election_data:

    #To do: read and analyze data here.

    #Read the file object with the reader funciton
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file
    #for row in file_reader:
       # print(row)

#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.