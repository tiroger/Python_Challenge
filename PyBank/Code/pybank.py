# Importing the necessary modules
import csv
import os

# Creating lists to contain all the months and revenue values
# Creating a list to contain the revenue changes between months
all_months = []
all_revenue = []
revenue_change = []

# Creating the file path for the data file
file_path = os.path.join('..', 'Resources', 'budget_data.csv' )

# Opening and reading the csv file
with open(file_path, 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    csv_header = next(read_csv)
    
     # Iterating through each row of the csv file.
        # Adding to the list containing all the months
        # Adding to the list containing al the revenue values
    for row in read_csv:
        all_months.append(row[0])
        all_revenue.append(int(row[1]))

    # Iterating once more through each row of the csv file
        # Adding the difference between consecutive months along the entirety of the list containing all the revenue values
    for i in range(1,len(all_revenue)):
        revenue_change.append(all_revenue[i] - all_revenue[i-1]) 
        
        #Calculating the average difference between revenues  
        avg_revenue_change = sum(revenue_change)/len(revenue_change)

        # Finding the largest and smallest values in the revenue change list
        max_revenue_change = max(revenue_change)
        min_revenue_change = min(revenue_change)

        # Finding the corresponding dates associated with change in revenue
            # Find the index value of the revenue change
            # Add 1 to the index to account for the fact that revenue change encompasses two values (months)
                # len(revenue_change) = 85 and len(all months) = 86
            # If we don't add 1, the index will correspond to the previous month
                # For example, index 0 will be the first value in the list. We want the change at index 0 + 1 = 1
        max_revenue_change_date = str(all_months[1 + revenue_change.index((max_revenue_change))])
        min_revenue_change_date = str(all_months[1 + revenue_change.index(min_revenue_change)])
        
# Finding the total number of months by determing the number of values in the all months list
total_months = len(all_months)

# Calculating the total revenue by summing the values contained in the all revenue list
total_revenue = sum((all_revenue))

# Print results table
print("Financial Analysis")
print("-------------------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average  Change: $("  + str(round(avg_revenue_change, 2)) + ")")
print("Greatest Increase in Profits: " + max_revenue_change_date + ' , $' + str(max_revenue_change))
print("Greatest Decrease in Profits: " + min_revenue_change_date +' , $('+ str(min_revenue_change) + ")")
print("-------------------------------------------------------")

# Creating the output path for the txt file
output_path = os.path.join('..', 'Output', 'pybank_analysis.txt' )

# Open the output file using "write" mode. 
# Specify the variable to hold the contents
with open(output_path, 'w', newline='') as results_file:

    # Write the desired text
    results_file.writelines("Financial Analysis" +'\n')
    results_file.writelines("-------------------------------------------------------" + '\n')
    results_file.writelines("Total Months: " + str(total_months) + '\n')
    results_file.writelines("Total Revenue: $" + str(total_revenue) + '\n')
    results_file.writelines("Average  Change: $("  + str(round(avg_revenue_change, 2)) + ")" + '\n')
    results_file.writelines("Greatest Increase in Profits: " + max_revenue_change_date + ' , $' + str(max_revenue_change) + '\n')
    results_file.writelines("Greatest Decrease in Profits: " + min_revenue_change_date +' , $('+ str(min_revenue_change) + ")" + '\n')
    results_file.writelines("-------------------------------------------------------" + '\n')

# Opening the output file in r mode and printing to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())
