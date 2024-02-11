# Filename: NRS528_CodingChallenge2.py
# Author: Elliot Vosburgh
# Date: 9 February 2024
# Description:
#
#	This file contains the answers to Coding Challenge 2.

#####################
# Part 1: List values
#####################

init_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]			# Define the initial list

selective_list = list(filter(lambda x: x < 5, init_list))	# Store values from init_list < 5 into selective_list;
								# This is an alternative I came up with to a "for" loop.

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

##################################################################
# Part 3: Given a single phrase, count the occurrence of each word
##################################################################

string = 'hi dee hi how are you mr dee'

uniques = len(set(string.split(" ")))		# Use the split() method to separate string by a single white space
						# Here I've learned both about set() and len(). A set is similar to a list
						# but can only contain unique values. By turning split_string into a set,
						# duplicate values are removed (i.e. {'dee', 'mr', 'how', 'hi', 'you', 'are'}.
						# Then len() takes care of counting how many values are stored in the set (6).

####################
# Part 4: User input
####################

years_left = 65 - (int(input("What is your age? ")))	# White space needed after question mark so the user doesn't type "...?_30".
							# Wrap everything in int() so it isn't a string.
							# Doing everything in one line just like I did in Part 3.

######################
# Part 5: User input 2
######################

letter_scores = {					# I'm using this table because I couldn't figure out how
        "a": 1, "e": 1, "i": 1, "o": 1,			# to find a letter within the multi-letter entries you gave
        "u": 1, "l": 1, "n": 1, "r": 1,			# (i.e. find a in aeioulnrst).
        "r": 1, "s": 1, "t": 1, "d": 2,
        "g": 2, "b": 3, "c": 3, "m": 3,
        "p": 3, "f": 4, "h": 4, "v": 4,
        "w": 4, "y": 4, "k": 5, "j": 8,
        "x": 8, "q": 10, "z": 10
}


user_word = list(input("Enter any word: ").lower())	# No need to use split() here, just pass the word into list().
							# There aren't white spaces in Scrabble, anyway...
							# Don't forget to make everything lowercase, else it will return
							# a "KeyError" for the first uppercase value it finds.


word_score = sum(letter_scores[i] for i in user_word)	# This was difficult until I learned of the sum() method.
