# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path
    
# Define variables to track the financial data
months = []
greatest_increase = 0
greatest_decrease = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []

greatest_increase_date = ""
greatest_decrease_date = ""
profit_loss = []
changes = [] 

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    #Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change


    # Process each row of data
    for row in reader:

            # Track the total
            total_net += int(row[1])
            profit_loss.append(int(row[1]))
            months.append(row[0])
    total_months = len(months)
    
    # Track the net change

    
    data = list(zip(months, profit_loss))

    # Calculate the greatest increase in profits (month and amount)
    # Greatest_increase -= int(row[1])
    for b in range(1, len(data)):
            change2 = data[b][1] - data[b-1][1]
            if change2 > greatest_increase:
                greatest_increase = change2
                greatest_increase_date = data[b][0] 
            
    
    # Calculate the greatest decrease in losses (month and amount)
    # Greatest_decrease -= int(row[1])

    for b in range(1, len(data)):
            change3 = data[b][1] - data[b-1][1]
            if change3 < greatest_decrease:
                greatest_decrease = change3
                greatest_decrease_date = data[b][0]


# Calculate the average net change across the months

    for i in range(1, len(profit_loss)):
            change = profit_loss[i] - profit_loss[i-1]
            changes.append(change)
    average_change = round(sum(changes) / len(changes), ndigits= 2)

# Generate the output summary
#output_summary = {}
#output_summary = dict()
#output_summary = {'Total Months': f'{total_months}','Total': f'{total_net}','Average':f'{average_change}','Greatest Increase in Profits': f'{greatest_increase,greatest_increase_date}','Greatest Decrease in Profits': f'{greatest_decrease,greatest_decrease_date}'}



# Print the output
output1 = "Financial Analysis"
output2 = "-----------------"
output3 = 'Total Months: ' f'{total_months}'
output4 = 'Total: ' f'${total_net}'
output5 = 'Average: ' f'${average_change}'
output6 = 'Greatest Increase in Profits: ' f' {greatest_increase_date} (${greatest_increase})'
output7 = 'Greatest Decrease in Profits: ' f' {greatest_decrease_date} (${greatest_decrease})'

# Write the results to a text file
with open(file_to_output, "w") as txt_file:

    print(output1)
    print(output2)
    print(output3)
    print(output4)
    print(output5)
    print(output6)
    print(output7)



    txt_file.write(output1)
    txt_file.write(f'\n{output2}')
    txt_file.write(f'\n{output3}')
    txt_file.write(f'\n{output4}')
    txt_file.write(f'\n{output5}')
    txt_file.write(f'\n{output6}')
    txt_file.write(f'\n{output7}')
