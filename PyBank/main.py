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
                greatestmonthinc = row[0]
            #if the current change is less then the previous change the greatest decrease now equals the change
            if change < greatestdecrease:
                greatestdecrease = change
                greatestmonthdec = row[0]
            
        previous=int(row[1])
        first_time= False

        

print(month_count)
print(net_total)
print(total_change/(month_count-1))
print(greatestmonthinc, + greatestincrease)
print(greatestmonthdec, + greatestdecrease)

        



    
# Specify the file to write to
output_path = os.path.join("analysis", "results.txt")


# Open the file using "write" mode. Specify the variable to hold the contents
f = open(output_path, 'w')
f.write("Financial Analysis \n")
f.write("---------------------------- \n")
f.write(f"Total Months: {month_count}\n")
f.write(f"Total: ${net_total} \n")
f.write(f"Average  Change: $ {total_change/(month_count-1)}\n")
f.write(f"Greatest Increase in Profits: {greatestmonthinc} (${greatestincrease})\n")
f.write(f"Greatest Decrease in Profits: {greatestmonthdec} (${greatestdecrease})")


   

