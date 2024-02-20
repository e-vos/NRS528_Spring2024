# Filename: NRS528_CodingChallenge2.py
# Author: Elliot Vosburgh
# Date: 9 February 2024
# Description:
#
#	This file contains the answers to Coding Challenge 2 Part 2

######################
# Part 2: List overlap
######################


list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

common_list = [i for i in list_a if i in list_b]
difference_list = [i for i in list_a + list_b if i not in list_a or i not in list_b]	# This took a while to figure out. Once I learned about the
											# "in" and "not in" operators, I used the alternative from
											# Part 1. First I concatenate the lists. Then, I iterate
											# through this concatenated list to find elements not in
											# list_a OR list_b.
											
print(common_list)
print(difference_list)