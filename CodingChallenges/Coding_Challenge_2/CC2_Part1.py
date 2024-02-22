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

selective_list = []

for i in init_list:

    if i < 5:

        selective_list.append(i)

selective_list_oneline = list(filter(lambda x: x < 5, init_list))	# Store values from init_list < 5 into selective_list;
                                                            # This is an alternative I came up with to a "for" loop.
								
print("Results of for loop method: " + str(selective_list))
print("Results of one-line method: " + str(selective_list_oneline))