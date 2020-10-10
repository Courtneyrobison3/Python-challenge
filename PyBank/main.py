import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    month_count =0
    net_total= 0

    for row in csvreader:
        month_count = month_count + 1 
        net_total = net_total + int(row[1])
    print(month_count)
    print(net_total)

        



    
# # Specify the file to write to
# output_path = os.path.join("..", "analysis", "results.csv")


# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'results') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])


