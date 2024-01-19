# Modules
import os
import csv



# set the path for the files
# Budget data file
budget_csv = os.path.join('Resources/budget_data.csv')
# Election data file
election_csv = os.path.join('Resources/election_data.csv')

#PyBank Analysis

# initializing a variable to store the total net value
net_total = 0
# Initializing an emty list to store the changes over the entire period
changes = []
# Initializing a value to store previous value
previous_change = None
previous = 0
max_increase = 0
max_decrease = 0
total_Month = 0
# assigning the month of the greatest increase and decrease
max_date = None
min_date = None

# Open the budget data CSV using the UTF-8 encoding
with open(budget_csv, encoding='UTF-8') as csvbudget:
    budget_reader = csv.reader(csvbudget, delimiter=',')
    
    # Skip the header row
    budget_header = next(budget_reader)

    # Loop through the first row (Date) to calculate the number of months
    for rowBudget in budget_reader:
       
        # assign the first row to variables
        months = rowBudget[0]
        profit_loss = int(rowBudget[1])

        # 1. Total Months
        # increament the count for the rows to get the total number of months
        total_Month += 1

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
print("\nFinancial Analysis\n")
print('----------------------------\n')
print(f'Total Months: {total_Month}\n')
print(f'Total: ${net_total}\n')
print(f'Average Change: ${avg:.2f}\n')
print(f'Greatest Increase in Profits: {max_date} (${max_increase})\n')
print(f'Greatest Decrease in Profits: {min_date} (${max_decrease})\n')
    

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
    budgetDataFile.write(f'Greatest Derease in Profits: {min_date} (${max_decrease})')

# ------------------------------------------------------------------------------------------- #
    
#PyPoll Analysis

# Open the election data CSV using the UTF-8 encoding
with open(election_csv, encoding='UTF-8') as csvelection:
    election_reader = csv.reader(csvelection, delimiter=',')

    # set the variables to values
    total_vote = 0
    candidate_name = None
    win_votes = 0
    winner = ""

    # Skip the first row
    election_header = next(election_reader)
    
    # set a dictionary and list to empty
    canDic = {}
    canList = []

    # Loop through the rows
    for rowElection in election_reader:

        # 1. total votes 
        # add 1 for every loop for every row to count the number of votes
        total_vote +=1

        # set the candidate to variable
        candidate = rowElection[2]

        # 2. List of candidates and total number of votes for each
        # assign the first value to candidate_name
        if candidate is not None:
            candidate_name = candidate
            # check if candidate name is not in the dictionary
            if candidate_name not in canDic:
                # if so, we add the name to the list
                canDic[candidate_name] = 1
                # if yes, we add one to the name to count the votes for each
            else: 
                canDic[candidate_name] += 1


        candidate_name = candidate # update the candidate name for the new row

# Set a variable for election Data output file
election_output = os.path.join('analysis/election_data_analysis.txt')
# Open the output file
with open(election_output, "w") as electionDataFile:

    # printing the result into the terminal
    print("\nElection Results\n")
    print('----------------------------\n')
    print(f'Total Votes: {total_vote}\n')
    print('----------------------------\n')

    # write into the text file
    electionDataFile.write("\nElection Results\n")
    electionDataFile.write('----------------------------\n')
    electionDataFile.write(f'Total Votes: {total_vote}\n')
    electionDataFile.write('----------------------------\n')

    # Loop therough the dictionary to find the votes and vote percentage for each candidate 
    for candidate_name, canVotes in canDic.items():

        # 3. Percentage of votes for each candidate
        # Calculate the percentage for the candidates
        perc = (canVotes / total_vote) * 100
        
        # 4. The winner of the election 
        # Condidtion to check the winner candidate
        if canVotes > win_votes:
            winner = candidate_name
        win_votes = canVotes # Updatine winVotes for the next row

        # Printing the resuls into the termibal and write into the text file
        print(f'{candidate_name}: {perc:.3f}% {(canVotes)}\n')
        electionDataFile.write(f'{candidate_name}: {perc:.3}% {canVotes}\n')

    print('----------------------------\n')    
    print(f'Winner: {winner}\n')   
    print('----------------------------')  
    electionDataFile.write('----------------------------\n')
    electionDataFile.write(f'Winner: {winner}')

    
    
    