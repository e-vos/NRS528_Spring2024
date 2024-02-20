# Filename: NRS528_CodingChallenge2.py
# Author: Elliot Vosburgh
# Date: 9 February 2024
# Description:
#
#	This file contains the answers to Coding Challenge 2 Part 1

#####################
# Part 1: List values
#####################

init_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]			# Define the initial list

selective_list = list(filter(lambda x: x < 5, init_list))	# Store values from init_list < 5 into selective_list;
								# This is an alternative I came up with to a "for" loop.
								
print(selective_list)