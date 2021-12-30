#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete liste of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

#Assign a variable for the file to load and the path.
file_to_load = 'election_results.csv'
#open the election results and read the file.
with open(file_to_load) as election_data:
   # To do : perform analysis.
   print(election_data)

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")
#open the election results and read the file.
with open (file_to_load) as election_data:
    print (election_data)

#create a filename variable to a direct or indirect path to the file.
File_to_save = os.path.join("analysis", "election.txt")
#using the open()function with "w" mode we will write date to the file.
open (File_to_save,"w")
#Using the with statement open the file as a text file.
with open (File_to_save, "w") as txt_file:
    # Write three counties to the file.
        txt_file.write("Counties in the Election\n")
        txt_file.write("-------------------------\n")
        txt_file.write("Arapahoe\n")
        txt_file.write("Denver\n")
        txt_file.write("Jefferson") 

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


        
