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

# print(annuals_dict)				