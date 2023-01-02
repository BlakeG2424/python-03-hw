# import dependencies
import os
import csv

# path to collect data
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Lists of stored data / declare variables
months = []
profit_loss = []
total_months = 0
net_total = 0
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
 
# open and read csv
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile)


# read the header row first
    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    net_total += int(first_row[1])
# define variable for use in calculating net change between months
    previous_net = int(first_row[1])

# read each row of data after the header
    for row in csv_reader: 
        total_months += 1
        net_total += int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        profit_loss.append(net_change)
        months.append(row[0])

# calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[1]=net_change
            greatest_increase[0]=row[0]


  # calculate greatest decrease       
        if net_change < greatest_decrease[1]:
            greatest_decrease[1]=net_change
            greatest_decrease[0]=row[0]   

# calculate average change (sum/len)

    sum_profit_loss = sum(profit_loss)
    average_profit_loss = round(sum_profit_loss/(total_months), 2)
#print(average_profit_loss)

#create string to hold 
output=(f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_profit_loss}
Greatest Increase in Profits: {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease}
""")

print(output)

# Specify the file to write to

output_path = os.path.join("analysis", "output.txt")

with open(output_path, "w") as text:
        text.write(f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_profit_loss}
Greatest Increase in Profits: {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease}
""")

   


