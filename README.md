# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Calculate the total number of votes came from each county.
3. Calculate the percentage of votes from each county.
4. Determine which county contributed the highest number of votes.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.

## Election-Audit Results
The analysis of the election show that:

There were 369,711 votes cast in the election.

The county results were:
    - Jefferson County contributed to 10.5% of the final vote with 38,855 number of votes.
    - Denver County contributed to 82.8% of the final vote with 272,892 number of votes.
    - Arapahoe County contributed to 6.7% of the final vote with 24,801 number of votes.

The County with the largest number of votes was Denver County

The candidate results were:
    - Charles Casper recieved 23% of the final vote and 85,213 number of votes.
    - Diana DeGette recieved 73.8% of the final vote and 272,892 number of votes.
    - Candidate 3 recieved 3.1% of the final vote and 11,606 number of votes.
 
 The winner of the election was Diana Degette with 73.8% of the final vote and 272,892 number of votes.

## Election-Audit Summary
The script I wrote for this election audit can be easily modified and used for any other election. I propose you use this script for future elections to save time and avoid errors.

This script pulls data from the election_data.csv file that was provided to me to perform this analysis. I use the file_to_load variable to locate the file on my drive by using the names of the folders the file is nested in and the name of the file in paraentheses separated by commas. I use the file_to_save variable to create a file for the results to be uploaded to for this particular election. By importing the os and csv modules, the script allows us to locate and update these files. The file_to_load and file_to_save_ variable can be easily modified to use towards the file for any election and to save the results under any file name by updating the values in the parentheses to be the relevent file names and folders the files are in.

(line 5-11 copy)

I set the variable candidate_name equal to the third row of the file where the candidate name info is located (candidate_name = row[2]). The row function returns the values from a row with a particular index. Indexes start at 0 for the first row, and so on, so the third row will have an index = 2. I used this same logic for the variable county_names which returns the values from the second row. It is likely that the rows will be different in other election data files so this can be easily modified by changing the index number to the rows with the correct info in the file being used.

(line 47-50 code copy)

Once the variables file_to_load, file_to_save, candidate_name, and county_name are updated for the election data file being used, the script will do the rest of the work for you, displaying the same format of results as the one used in the current eletion audit!
(SS of text file)
