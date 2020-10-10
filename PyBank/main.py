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
    value = 0
    next_value = 0
    previous = 0 
    total_change =0
    first_time = True 
    greatestincrease = 0
    greatestdecrease = 9999999999
    


    for row in csvreader:
        month_count = month_count + 1 
        net_total = net_total + int(row[1])

        if not first_time:
            change=int(row[1])- previous
            total_change = total_change + change

            #if the current change is great then previous change now grestest change = current one.
            if change > greatestincrease:
                greatestincrease = change
            if change < greatestdecrease:
                greatestdecrease = change
                
            
        previous=int(row[1])
        first_time= False

        




print(month_count)
print(net_total)
print(total_change/(month_count-1))
print(greatestincrease)
print(greatestdecrease)
        



    
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


