import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "output.csv")
# Initializing variables used in the code
output_map = {}
diff_map = {}
total = 0

# Read the budget_data.csv file
# Iterate the rows from the csv file and put the values in the dictionary
# Key = date; value = Profit/losses 
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        output_map.update({row[0]:int(row[1])})

# Iterate the dictionary to get a new dictionary
# Key in new dictionary = date; value in new dictionary = difference between profits from next row and the current row
for index, output in enumerate(output_map):
    if(index >= len(output_map)-1) : break
    next_value = list(output_map.values())[index+1]
    current_value = list(output_map.values())[index]
    diff = next_value - current_value
    key = list(output_map.keys())[index+1]
    diff_map.update({key:diff})

total_months = len(output_map)
total = sum(output_map.values())
average_change = round(sum(diff_map.values())/len(diff_map),2)
profit_increase = max(diff_map.values())
profit_decrease = min(diff_map.values())
profit_increase_date = list(diff_map.keys())[list(diff_map.values()).index(profit_increase)]
profit_decrease_date = list(diff_map.keys())[list(diff_map.values()).index(profit_decrease)]

#Write the results to the output file
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis")
    print("Financial Analysis")
    output_file.write("\n----------------------------------------------------")
    print("----------------------------------------------------")
    output_file.write(f'\nTotal Months: {total_months}')
    print(f'Total Months: {total_months}')
    output_file.write(f'\nTotal: ${total}')
    print(f'Total: ${total}')
    output_file.write(f'\nAverage Change: ${average_change}')
    print(f'Average Change: ${average_change}')
    output_file.write(f'\nGreatest Increase in Profits: {profit_increase_date} (${profit_increase})')
    print(f'Greatest Increase in Profits: {profit_increase_date} (${profit_increase})')
    output_file.write(f'\nGreatest Decrease in Profits: {profit_decrease_date} (${profit_decrease})')
    print(f'Greatest Decrease in Profits: {profit_decrease_date} (${profit_decrease})')
