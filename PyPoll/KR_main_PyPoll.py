
# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(r"C:\Users\katro\python-challenge\PyPoll\Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join(r"C:\Users\katro\python-challenge\PyPoll\analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes= {}

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = ['Charles Casper Stockham', 'Diana Degette','Raymon Anthony Doane' ]

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load,encoding='UTF-8') as election_data:
    reader = csv.reader(election_data, delimiter=',')

    # Skip the header row
    header = next(reader)
       
    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes +=1 # Increment the total vote count for each row
     

        candidate= row[2]# Get the candidate's name from the row
        
        #If the candidate is not already in the candidate list, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate]= 0
            
        # Add a vote to the candidate's count
        candidate_votes[candidate]+= 1

    # Print the total vote count (to terminal)
    print('Election Summary')
    print(f'Total Vote Count:{total_votes}')

    # Loop through the candidates to determine vote percentages and identify the winner
        # Print and save each candidate's vote count and percentage
    for candidate, votes in candidate_votes.items():
        percentage=(votes/total_votes)*100  # Get the vote count and calculate the percentage
        print(f'{candidate}: {percentage:.3f}% ({votes})')
        

    # Generate and print the winning candidate summary
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"Winner: {winner}")

    header = 'Election Results'
    subheader = '---------------------'

# Open a text file to save the output
with open(file_to_output, "w",newline='') as txt_file:
    writer = csv.writer(txt_file)

    writer.writerow([header])
    writer.writerow([subheader])
    
    writer.writerow([f'Total Vote Count:{total_votes}']) # Write the total vote count to the text file
    writer.writerow([subheader])

    for candidate, votes in candidate_votes.items():
        percentage= (votes/total_votes)*100
        writer.writerow([f'{candidate}: {percentage:.3f}% ({votes})'])

    writer.writerow([subheader])
    writer.writerow([f"Winner: {winner}"]) # Save the winning candidate summary to the text file

