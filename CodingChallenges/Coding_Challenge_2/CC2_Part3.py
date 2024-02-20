# Filename: NRS528_CodingChallenge2.py
# Author: Elliot Vosburgh
# Date: 9 February 2024
# Description:
#
#	This file contains the answers to Coding Challenge 2 Part 3

##################################################################
# Part 3: Given a single phrase, count the occurrence of each word
##################################################################

string = 'hi dee hi how are you mr dee'

uniques = len(set(string.split(" ")))		# Use the split() method to separate string by a single white space
						# Here I've learned both about set() and len(). A set is similar to a list
						# but can only contain unique values. By turning split_string into a set,
						# duplicate values are removed (i.e. {'dee', 'mr', 'how', 'hi', 'you', 'are'}.
						# Then len() takes care of counting how many values are stored in the set (6).

print(uniques)