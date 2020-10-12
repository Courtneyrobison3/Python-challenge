import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')
#create null dictionary to store candidate names
candidate_name = {}
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents 
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
#define variables
    votes = 0
    candidates = {}
    
    #determine the number of votes cast by counting t

# determine the number of votes cast by counting the number of voter IDs
    for row in csvreader:
        votes = votes + 1

    
        
        #loop through and find the 

        if row[2] not in candidates:
           # candidates[row[2]] = 1
            candidates.update({row[2] : 1})
        else:
            candidates[row[2]] += 1
             
    
print(candidates)
print(int(votes))