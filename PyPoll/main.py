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
           
            candidates.update({row[2] : 1})
        else:
            candidates[row[2]] += 1
    print(int(votes))         
    print(candidates)
    Cname = ""
    winner = 0
    for name in candidates:
        Vpercent = (candidates[name]/votes)*100
        print(Vpercent)
        percent = print(Vpercent)
        #canditate with most votes wins.
        
        if candidates[name] > winner:
            winner = candidates[name]
            Cname =  name
    print(Cname  + str(winner))

    # Specify the file to write to
    output_path = os.path.join("analysis", "results.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
f = open(output_path, 'w')
f.write("Election Results \n")
f.write("---------------------------- \n")
f.write(f"Total Votes: {votes}\n")
f.write("---------------------------- \n")
f.write(f"{percent} \n")
# f.write(f"Average  Change: $ {total_change/(month_count-1)}\n")
# f.write(f"Greatest Increase in Profits: {greatestmonthinc} (${greatestincrease})\n")
f.write(f"Winner: {(Cname)} ")



            
        


        
    