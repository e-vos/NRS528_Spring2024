# Filename: NRS528_CodingChallenge2.py
# Author: Elliot Vosburgh
# Date: 9 February 2024
# Description:
#
#	This file contains the answers to Coding Challenge 2 Part 4

####################
# Part 4: User input
####################

years_left = 65 - (int(input("What is your age? ")))	# White space needed after question mark so the user doesn't type "...?_30".
							# Wrap everything in int() so it isn't a string.
							# Doing everything in one line just like I did in Part 3.
							
print(years_left)