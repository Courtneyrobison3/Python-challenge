import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

 # Specify the file to write to
output_path = os.path.join("analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
f = open(output_path, 'w')
f.write("Election Results \n")
f.write("---------------------------- \n")

with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents 
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    
#define variables
    votes = 0
    candidates = {}

# determine the number of votes cast by counting the number of voter IDs
    for row in csvreader:
        votes = votes + 1
        
        #loop through and find the votes per candidate

        if row[2] not in candidates:
           
            candidates.update({row[2] : 1})
        else:
            candidates[row[2]] += 1

    f.write(f"Total Votes: {votes}\n")
    f.write("---------------------------- \n")        
    print(F"Election Results")
    print(f"Total Votes: {votes}")         
    #create variable to determine winner
    Cname = ""
    winner = 0
    #calculate the precentages of votes each candidate recieved
    for name, vote in candidates.items():
        Vpercent = (vote/votes)*100
        print(f"{name}: {Vpercent:.3f}% ({vote})")
        f.write(f"{name}: {Vpercent:.3f}% ({vote})\n")
        
        #canditate with most votes wins.
        #determine the winner by comparing the number of votes to eachother
        if candidates[name] > winner:
            winner = candidates[name]
            Cname =  name
    print(f"Winner: {(Cname)} ")
  
# f.write(f"Greatest Increase in Profits: {greatestmonthinc} (${greatestincrease})\n")
f.write(f"Winner: {(Cname)} ")



            
        


        
    