# Filename: NRS528_CodingChallenge3_Part3.py
# Author: Elliot Vosburgh
# Date: 10 February 2024
# Description:
#
#	This file contains my answers to Coding Challenge 3 Part 3.

##########################
# Part 3: Working with CSV
##########################

import csv

years = []		# Create a list to store YYYY from the date column
annuals_dict = {}	# Dictionary for use later on...
ppm_values = []		# For the second task

# Find unique YYYY values, to iterate through the ppm values

with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

	next(co2)

	for row in csv.reader(co2):

		date = row[0]			# This block splits row[0] by hyphens into a list, then grabs the first 
		year = date.split('-')[0]	# item in the list (i.e. the year in YYYY format).
		years.append(year)		# Then add it to the years list

years_set = sorted(list(set(years)))		# Turn it into a set to get unique years, turn it back into a list, then
						# sort it in ascending order.

# Now for iterating through the ppm column by the items in years_set

for year in years_set:

	with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

		summed_values = float(0)	# Need float here because the ppm values are floats
		count_values = 0		# Count can be an integer

		next(co2)

		for row in csv.reader(co2):

			if str(year) in str(row[0]):			# Check if these are the values we're looking for 

				summed_values += float(row[1])		# Sum all of the ppm values found with the current year index
				count_values += 1			# Count how many ppm values have been summed

			if count_values != 0:				# Best practice for the future, yes?

				annual_avg = float(summed_values/count_values)		# Calculate average ppm value for the year
				annuals_dict[year] = annual_avg				# Associate the average with the year, in the
											# dictionary (e.g. 1959 | 300).

print("Contents of annuals dictionary = " + str(annuals_dict))

# Find the minimum, maximum, and average values for the entire dataset

with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

	summed_values = float(0)	# Same as in Task 1
	count_values = 0

	next(co2)

	for row in csv.reader(co2):

		ppm = row[1]
		ppm_values.append(ppm)
		summed_values += float(ppm)
		count_values += 1

	srt_ppm_values = sorted(ppm_values)		# Need to sort these for the next steps

	min_ppm = srt_ppm_values[0]			# Since ppm values are sorted numerically, 1st item = minimum
	max_ppm = srt_ppm_values[-1]			# and last item = maximum.
	avg_ppm = summed_values/count_values

print("Minimum ppm value = " + str(min_ppm))
print("Maximum ppm value = " + str(max_ppm))
print("Average ppm value = " + str(avg_ppm))

# Seasonal average in Spring, Summer, Fall, and Winter

ppm_values = []				# Reset the list from Task 2

seasons = {'spring': ["03", "04", "05"], 'summer': ["06", "07", "08"],			# Create a seasons dictionary
		'fall': ["09", "10", "11"], 'winter': ["12", "01", "02"]}

monthly_dict = {}	# Storage for monthly averages
seasonal_avgs = {}	# Storage for seasonal averages

for month in all_months:

	with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

		summed_values = float(0)
		count_values = 0

		next(co2)

		for row in csv.reader(co2):

			if str(month) in str(row[0]):			# Iterate by month

				ppm = row[1]				# Same as Task 2
				ppm_values.append(ppm)
				summed_values += float(ppm)
				count_values += 1

		monthly_avg = float(summed_values/count_values)		# " "
		monthly_dict[month] = monthly_avg

print("Contents of monthly dictionary: " + str(monthly_dict))

for season, mm in seasons.items():					# Using the items() method here to get seasons dictionary
									# items.
	season_values = [monthly_dict[month] for mm in months]		# Extract values based on the month key in monthly_dict
	seasonal_avgs[season] = sum(season_values)/len(season_values)	# Calculate seasonal averages and associate with season keys

print("Seasonal averages = " + str(seasonal_avgs))

# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

anomalies = {}	# Dictionary to store anomaly values

with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

	next(co2)

	for row in csv.reader(co2):

		position = row[1].index			# Get position of the current row. I could have used the date, but positions
							# are unique. The date might not be.

		anomaly = float(row[1]) - avg_ppm	# Calculate anomaly value for the current ppm value based on avg_ppm (Task 2)
		anomalies[position] = anomaly		# Store the position as key and anomaly as its value in the dictionary
        
print("Anomalies = " + str(anomalies))