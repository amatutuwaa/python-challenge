# Importing Modules
import os 
import csv

# Defining path and for csv file
election_data_csv = os.path.join("/Users/amatutuwaaosei-akoto/Desktop/python-challenge/PyPoll/resources/election_data.csv")

# Storing candidates vote counts
candidates_vote_count =  {}

# Storing vote counts percentage
vote_percentage = {}

# Variable to hold total vote count
total_votes = 0

# Variable to hold the winner count
winner_count = 0


with open (election_data_csv, newline="") as csvfile:
    election_data_reader = csv.reader(csvfile, delimiter=",")
    
    # Skipping the header row
    next(election_data_reader)
    
    # looping through the rows of data
    for row in election_data_reader:
        
        # Counting total votes 
        total_votes += 1
        
        # Counting total votes for each candidate
        if row[2] in candidates_vote_count:
            candidates_vote_count[row[2]] += 1
        
        else:
            candidates_vote_count[row[2]] = 1

# Calculating the percent of votes for each candidate:
for candidate in candidates_vote_count:
    vote_percentage[candidate] = (candidates_vote_count[candidate] / total_votes) * 100
    
    # Determining the winner based on popular vote
    if candidates_vote_count[candidate] > winner_count:
        winner_count = candidates_vote_count[candidate]
        winner = candidate
        
# Initialising the txt file for the results
results_path = os.path.join('election_results.txt')
        
with open(results_path, 'w', newline="") as textfile:
    
    textfile.write(f'''
Eletion Results
-----------------------------
Total Votes:  {total_votes}
-----------------------------\n''')
    
    print(f'''\nElection Results
-----------------------------
Total Votes:{total_votes}
-----------------------------''')
    
    for candidate, votes in candidates_vote_count.items():
        textfile.write(f'{candidate}: {vote_percentage[candidate]:.3f}% ({votes})\n')
        print(f'''{candidate}: {vote_percentage[candidate]:.3f}% ({votes})''')                

    textfile.write(f'''---------------------------- 
Winner: {winner}
----------------------------''')

    print (f'''-----------------------------")
Winner: {winner}
----------------------------''')




# Printing the resutls on terminal
# print (f"Election Results")
# print (f"-------------------------------")
# print (f"Total Votes: {total_votes}")
# print (f"-------------------------------")
# for candidate, votes in candidates_vote_count.items():
    # print (candidate, ": ", str(candidates_vote_count[candidate]), "% ", votes)
# print (f"-------------------------------")
# print (f"Winner: {winner}")
#print (f"-------------------------------")

