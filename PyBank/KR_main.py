
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(r"C:\Users\katro\python-challenge\PyBank\Resources", "budget_data.csv")# Input file path
file_to_output = os.path.join(r"C:\Users\katro\python-challenge\PyBank\analysis", "budget_.txt")# Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0.0

# Add more variables to track other necessary financial data
net_change = 0
great_increase = 0
great_increase_date=""
great_decrease = 0
great_decrease_date=""

# Open and read the csv
with open(file_to_load,encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    header = next(reader)
    print(header)

    # Extract first row to avoid appending to net_change_list

    # Process each row of data
    for row in reader:
        total_months +=1 #Track total months
        total_net += float(row[1])# Track the total

        # Calculate the greatest increase in profits (month and amount)
        if int(row[1]) > great_increase:
            great_increase = int(row[1])
            great_increase_date = (row[0])

        # Calculate the greatest decrease in losses (month and amount)
        if int(row[1]) < great_decrease:
            great_decrease = int(row[1])
            great_decrease_date = (row[0])

    print(f'Total Months:{total_months}')  
    print(f'Total Net:{total_net}')
    print(f'Greatest Increase:{great_increase_date} (${great_increase})')
    print(f'Greatest Decrease:{great_decrease_date} (${great_decrease})')
    

# Track the total and net change
    #net_change_list=list(reader)
    #net_change = 
    #print(f'Net Change: (${net_change})')

# Track the net change, average

# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
with open(file_to_output,'w') as txt_file:
    txt_file.write("budget_.txt")



#Notes: Your task is to create a Python script that analyzes the records to calculate each of the following values:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period