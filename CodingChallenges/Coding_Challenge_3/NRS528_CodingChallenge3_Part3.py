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

# Calculate annual averages

with open("co2-ppm-daily.csv") as co2:

	years = []					# Blank lists for years and ppm values
	ppm = []

	next(co2)					# Skip the first row (headings)

	for row in csv.reader(co2):			# Iterate through each row in the file

		date = row[0]				# Since we're working per row, row[0] will
		value = float(row[1])			# always be a date and row[1] will always be
		year = date.split('-')[0]		# a ppm value. Find year by splitting date into
							# a list and grabing the first item in said list.

		years.append(year)			# Each row, add the year to years[]
		ppm.append(value)			# Each row, add the ppm value to averages[]. Even
							# though it's still just a ppm value, later I'll
							# average them.

	years_set = list(set(years))			# Back to sets. We need it to be a set to have only
	srt_years = sorted(years_set)			# unique year values. Then sort it (1958, 1959, etc.)

averagesDict = {}					# Create a blank dictionary where I'll store unique years
							# (from srt_years) and the respective ppm annual averages

for year in srt_years: