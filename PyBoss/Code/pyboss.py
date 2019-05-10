# Importing the modules
import csv
import os
from operator import itemgetter
from datetime import datetime

# state abbreviation library
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Create file path names for input
file_path = os.path.join('..', 'Resources', 'employee_data.csv')

# Opening and reading the csv file
with open(file_path, 'r') as csv_file:
	read_csv = csv.reader(csv_file, delimiter=',')
	csv_header = next(read_csv)

	# Creating new lists to capture:

	# Employee ID
	emp_id =[]

	# Names and split names
	names = []
	split_names = []
	
	# DOB and converted DOB
	dob = []
	converted_dob = []

	# States and converted states
	states = []
	converted_states =[]

	# SSN and hidden hidden_ssn
	ssn = []
	hidden_ssn = []

	# Iterating through the names column to capture all the names in names list
	for row in read_csv:
		emp_id.append(row[0])
		names.append(row[1])
		dob.append(row[2])
		ssn.append(row[3])
		states.append(row[4])

	# Iterating trhough the list of names split the names using the space (' ') delimiter
		# Adding each split names to the list of split names
	for name in names:
		split_names.append(name.split(' '))

	# Creating two lists: First Names and Last Names
	first_name = list(map(itemgetter(0), split_names))
	last_name = list(map(itemgetter(1), split_names))

	# Iterating through the entire list using range
	for i in range(len(emp_id)):

		# Modifying DOB using datetime module
		date_strip = datetime.strptime(dob[i], '%Y-%m-%d').strftime('%m/%d/%Y')
		converted_dob.append(date_strip)

		# Modifying ssn to hide he first five numbers
		# Concatenating the mask with the last 4 digits of each ssn
		ssn_masked = "***-**-" + ssn[i][-4:]
		hidden_ssn.append(ssn_masked)

		# Modifying state names to state abbrevations
		# Using the dictionary of states to match the state name (key) with its two letter abbreviation (value)
		state_two_letter = us_state_abbrev[states[i]]
		converted_states.append(state_two_letter)

	# Create file path names for output
	output_path = os.path.join('..', 'Output', 'cleaned_employee_data.csv')

	# Creating new headers and combining converted values into a new list of lists
	cleaned_employee_data_header = [('Employee ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State')]
	cleaned_employee_data_values = zip(emp_id, first_name, last_name, converted_dob, hidden_ssn, converted_states)

	with open(output_path, 'w', newline='') as converted_data:
		writer = csv.writer(converted_data)

		# Writing the new header and values
		writer.writerows(cleaned_employee_data_header)
		writer.writerows(cleaned_employee_data_values)






