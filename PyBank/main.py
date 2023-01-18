# Importing Modules
import os 
import csv

# Defining path for csv file 
budget_data_csv = os.path.join("/Users/amatutuwaaosei-akoto/Desktop/python-challenge/PyBank/resources/budget_data.csv")

# Storing data
total_months = 0
net_total = 0
second_row = 0
first_row = 0
month_change = 0
total_month_change = []
date = []

# Opening the CSV File
with open(budget_data_csv, newline="") as csvfile:
    budget_csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Skipping the header row
    csv_header = next(budget_csv_reader)
    
    # Looping through the csv file
    for row in budget_csv_reader:
        
        # Consolidating total months in budget csv        
        total_months += 1

        # Calculating the net total amount of Profit/Losses over entire period of time
        first_row = int(row[1])
        net_total += int(row[1])

        # Calculating the average changes each month 
        if (total_months==1):
            second_row = first_row
        else:
            month_change = first_row - second_row
            date.append(row[0])
            total_month_change.append(month_change)
            second_row = first_row

    average_change = round(sum(total_month_change)/(total_months - 1), 2) 

    # Calculating the greatest increase in profits
    max_profit = max(total_month_change)

    # Finding the date using the index of the greatest increase in profits
    index_max_profit = date[total_month_change.index(max_profit)]
    
    # Calculating the greatest decrease in profits
    min_profit = min(total_month_change)

    # Finding the date using the index of the greatest decrease in profits
    index_min_profit = date[total_month_change.index(min_profit)]


final_analysis = (f'''Financial Analysis
-------------------------------
Total months: {total_months}
Total: ${net_total:.2f}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {index_max_profit} (${max_profit:.2f})
Greatest Decrease in Profits: {index_min_profit} (${min_profit:.2f})''')

# Printing the analysis to the terminal 
print (final_analysis)

# Creating a txt file with the analysis

analysis = open('final_analysis.txt', 'w')
analysis.write(final_analysis)
analysis.close()






        
    
