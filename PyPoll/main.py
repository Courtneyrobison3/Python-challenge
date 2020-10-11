import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    votes = 0
# determine the number of votes cast by counting the number of voter IDs
    for row in csvreader:
        votes = votes + 1

       
    print(int(votes))