# Importing the necessary modules
import csv
import os
import operator

# Creating lists of values for all the votes and all the candidates
votes =[]
candidates = []

# Creating the file path for the data file
file_path = os.path.join('..', 'Resources', 'election_data.csv')

# Opening and reading the csv file
with open(file_path, 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    csv_header = next(read_csv)
    # Iterating through all rows of voter ID column
    for row in read_csv:
        # Adding all the votes to a list
        votes.append(row[0])
        # Adding all the candidates to a list
        candidates.append(row[2])

    # Calculating the total votes by counting the number of values in the list of votes
    total_votes = (len(votes))

    # Creating a dictionary with the number of times (value) each name (key) appears on the list
    vote_tally = {}

    # Iterating through the list of candidates
        # If the name is present in the dictionary, add 1 more vote
    for name in candidates:
        if name in vote_tally:
            vote_tally[name] += 1
        # If the name is not present in the dictionary, add the name
        else:
            vote_tally[name] = 1
    #print(vote_tally)

    # Calculating the number of votes and the percentage for each candidate
    khan_votes = vote_tally['Khan']
    khan_percent = round(100 * (khan_votes / total_votes), 3)

    correy_votes = vote_tally['Correy']
    correy_percent = round(100 * (correy_votes / total_votes), 3)

    li_votes = vote_tally['Li']
    li_percent = round(100 * (li_votes / total_votes), 3)
    
    otooley_votes = vote_tally["O'Tooley"]
    otooley_percent = round(100 * (otooley_votes / total_votes), 3)

    election_winner = max(vote_tally.items(), key=operator.itemgetter(1))[0]

    # Printing results table
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print("Khan: " + str(khan_percent) + '% (' + str(khan_votes) + ')')
    print("Correy: " + str(correy_percent) + '% (' + str(correy_votes) + ')')
    print("Li: " + str(li_percent) + '% (' + str(li_votes) + ')')
    print("O'Tooley: " + str(otooley_percent) + '% (' + str(otooley_votes) + ')')
    print("-------------------------")
    print('Winner: ' + election_winner)
    print("-------------------------")

# Creating the output path for the txt file
output_path = os.path.join('..', 'Output', 'pypoll_results.txt' )

# Open the output file using "write" mode. 
# Specify the variable to hold the contents
with open(output_path, 'w', newline='') as election_results:

    # Write the desired text
    election_results.writelines("Election Results" +'\n')
    election_results.writelines("-------------------------" +'\n')
    election_results.writelines("Total Votes: " + str(total_votes) +'\n')
    election_results.writelines("-------------------------" +'\n')
    election_results.writelines("Khan: " + str(khan_percent) + '% (' + str(khan_votes) + ')' +'\n')
    election_results.writelines("Correy: " + str(correy_percent) + '% (' + str(correy_votes) + ')' +'\n')
    election_results.writelines("Li: " + str(li_percent) + '% (' + str(li_votes) + ')' +'\n')
    election_results.writelines("O'Tooley: " + str(otooley_percent) + '% (' + str(otooley_votes) + ')' +'\n')
    election_results.writelines("-------------------------" +'\n')
    election_results.writelines('Winner: ' + election_winner +'\n')
    election_results.writelines("-------------------------" +'\n')

# Opening the output file in r mode and printing to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())






    


