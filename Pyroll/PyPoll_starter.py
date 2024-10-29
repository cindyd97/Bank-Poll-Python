# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
votes = []
all_votes = []
stockham = []
degette = []
doane = []
Winner = ''
highest_votes = 0
  

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

       # store total votes for later calculation
        all_votes.append(row[2])
        votes.append(row[0])
    total_votes = len(votes)


#count votes of each candidate
#Stockham
     
    for i in all_votes:
        if i == 'Charles Casper Stockham':
            stockham.append(i)
    total_stockham = len(stockham)
    percent_stockham = (total_stockham / len(all_votes))
    
 #Degette
    for i in all_votes:
        if i == 'Diana DeGette':
            degette.append(i)
    total_degette = len(degette)
    percent_degette = (total_degette / len(all_votes)) 
    
#Doane     
    for i in all_votes:
        if i == 'Raymon Anthony Doane':
            doane.append(i)
    total_doane = len(doane)
    percent_doane = (total_doane / len(all_votes)) 
   
 #Find the winner among the candidates   
    votes2 = {'Diana Degette': total_degette,'Raymon Anthony Doane':total_doane,'Charles Casper Stockham':total_stockham}
    for candidate, vote_count in votes2.items():
        if vote_count > highest_votes:
            highest_votes = vote_count
            Winner = candidate
        
 #organize output of information

output1 = "Election Results"
output2 = '----------------------'
output3 = 'Total Votes: ' f'{total_votes}'
output4 = '----------------------'
output5 = 'Charles Casper Stockham: ' f'{percent_stockham: .3%} ({total_stockham})'
output6 = 'Diana Degette: ' f'{percent_degette: .3%} ({total_degette})'
output7 = 'Raymon Anthony Doane: ' f'{percent_doane: .3%} ({total_doane})'
output8 = '----------------------'
output9 = 'Winner: ' f'{Winner}'





# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(output1)
    print(output2)
    print(output3)
    print(output4)
    print(output5)
    print(output6)
    print(output7)
    print(output8)
    print(output9)
    
     
    # Write the total vote count to the text file
    txt_file.write(output1) 
    txt_file.write(f'\n{output2}')
    txt_file.write(f'\n{output3}')
    txt_file.write(f'\n{output4}')
    txt_file.write(f'\n{output5}')
    txt_file.write(f'\n{output6}')
    txt_file.write(f'\n{output7}')
    txt_file.write(f'\n{output8}')
    txt_file.write(f'\n{output9}')


    

    
    
