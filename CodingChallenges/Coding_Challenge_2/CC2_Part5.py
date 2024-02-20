# Filename: NRS528_CodingChallenge2.py
# Author: Elliot Vosburgh
# Date: 9 February 2024
# Description:
#
#	This file contains the answers to Coding Challenge 2 Part 5

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

print("Scrabble score: " + word_score)