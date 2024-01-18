# Modules
import os
import csv



# set the path for the files
# Budget data file
budget_csv = os.path.join('Resources/budget_data.csv')
# Election data file
election_csv = os.path.join('Resources/election_data.csv')

# initializing a set to store months
monthly = set()
# initializing a variable to store the total net value
net_total = 0
# Initializing an emty list to store the changes over the entire period
changes = []
# Initializing a value to store previous value
previous_change = None
previous = 0
max_increase = 0
max_decrease = 0
# assigning the month of the greatest increase and decrease
max_date = None
min_date = None


# Open the budget data CSV using the UTF-8 encoding
with open(budget_csv, encoding='UTF-8') as csvbudget:
    budget_reader = csv.reader(csvbudget, delimiter=',')
    
    # Skip the header row
    budget_header = next(budget_reader)

    # Loop through the first row (Date) to calculate the umber of months
    for rowBudget in budget_reader:
       
        # assign the first row to variables
        months = rowBudget[0]
        profit_loss = int(rowBudget[1])

         # 1. Total Months
        # adding months into the monthly set
        monthly.add(months)
        # creating a variable that store the total number of the months by using (len)
        total_Month = len(monthly)

        # 2. Net Total 
        # creating a variable to hold the profit_loss values and add them to get the total value
        net_total += profit_loss


        # # 3. Average changes
        # check if the row is not empty
        if previous_change is not None:
            # calculate the change
            change = profit_loss - previous_change
            # adding the change to to the changes list
            changes.append(change)
        previous_change = profit_loss # Update the previous value
        

        # 4. Greatest increase & 5. Greatest decrease
        # assign values for the first row
        if months is None:
            max_date = months
            previous = profit_loss
        # calculate the changes
        else:
            increase = profit_loss - previous
            # condition to check the greater increase
            if increase > max_increase:
                max_increase = increase
                max_date = months
            # condition to check the greater decrease
            if increase < max_decrease:
                max_decrease = increase
                min_date = months
        previous = profit_loss # update the previous value

        
        
# calculating the average by adding the total changes and devid it by the length of the changes
avg = sum(changes) / len(changes)

# printing the result into the terminal
print("Financial Analysis")
print('----------------------------')
print(f'Total Months: {total_Month}')
print(f'Total: ${net_total}')
print(f'Average Change: ${avg:.2f}')
print(f'Greatest Increase in Profits: {max_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {min_date} (${max_decrease})')
    

# Set a variable for Budget Data output file
budget_output = os.path.join('analysis/budget_data_analysis.txt')
# Open the output file
with open(budget_output, "w") as budgetDataFile:
    # write into the text file
    budgetDataFile.write("Financial Analysis\n")
    budgetDataFile.write('----------------------------\n')
    budgetDataFile.write(f'Total Months: {total_Month}\n')
    budgetDataFile.write(f'Total: ${net_total}\n')
    budgetDataFile.write(f'Average Change: {avg:.2f}\n')
    budgetDataFile.write(f'Greatest Increase in Profits: {max_date} (${max_increase})\n')
    budgetDataFile.write(f'Greatest Derease in Profits: {min_date} (${max_decrease})\n')
