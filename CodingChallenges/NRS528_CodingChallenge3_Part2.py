# Filename: NRS528_CodingChallenge3_Part2.py
# Author: Elliot Vosburgh
# Date: 10 February 2024
# Description:
#
#	This file contains my answers to Coding Challenge 3 Part 2.


####################################
# Part 2: Push sys.argv to the limit
####################################

import sys
sys.stderr.write("Think carefully: what three numbers have the same sum and product?\n")
user_guess = set()
num_list = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
actual = set()
actual.update(num_list)
for i in range(3):
	number = int(input("Enter one number and press enter: "))
	user_guess.add(number)
ordered_guess = sorted(user_guess)
if actual == set(ordered_guess):
	print("Nice one.")
else:
	print("No... that's not right. The correct numbers were " + sys.argv[1] + ", " + sys.argv[2] + ", and " + sys.argv[3])