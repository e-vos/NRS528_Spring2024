# Filename: NRS528_CodingChallenge3_Part1.py
# Author: Elliot Vosburgh
# Date: 10 February 2024
# Description:
#
#	This file contains my answers to Coding Challenge 3 Part 1.

#####################
# Part 1: List values
#####################

import os		# I learned about the rmtrees function within the 'shutil' module
import shutil		# and decided to try using it, as the challenge prompt said nothing
			# about only being able to use 'os' in our deletions.

file_path = r"C:\CodingChallenge3"	# Set the file path. I found that CodingChallenge3 is created
					# in the first for loop, so I didn't have to write mkdirs twice.
					# The way the code works means you don't need CodingChallenge3
					# to hold everything, because it won't delete the primary
					# directory. That said, I thought it was safer to have it.

# I also didn't want to write out os.mkdirs every time I created a directory, so I made a list of the required directory names. I used \ as an escape character.

dir_list = ['draft_code', 'draft_code\\pending', 'draft_code\\complete', 'includes', 'layouts\\default', 'layouts\\post\\posted', 'layouts', 'layouts\\post', 'site']

for i in dir_list:					# For this loop, I iterate through the directory list and join it to file_path
	war_path = os.path.join(file_path, i)		# using 'os.path.join()' to create war_path.
	os.makedirs(war_path, exist_ok = True)		# Then I make the directories. If it already exists, (as when I was testing this
							# multiple times), it just overwrites the old directory without throwing me an
							# error. Thanks, Python.

def count_subs(i):					# Here's where things get tricky. I want to delete the directories with rmtree(),
	return i.count('\\')				# but if I do it in the order that dir_list is in, it won't delete everything.
							# I need to delete the directories based on their hierarchy from low to high.

sorted_dir_list = sorted(dir_list, key = count_subs, reverse = True)	# So, I count how many \\ exist in each dir_list item, order them
									# based on that value, then reverse the order.

# print(sorted_dir_list)

for i in sorted_dir_list:									# Now it's time to burn the bridges.
    burnt_bridges = os.path.join(file_path, i)							# I iterate through sorted_dir_list in the same way that I did in the first for loop.
    try:											# Then I attempt to delete the directories in that order. If it deletes it, it prints
        shutil.rmtree(burnt_bridges)								# that it was successful (i.e. bridge burned).
        print(f"Burned {burnt_bridges}. Let's see the rebels try to cross the river now!")
    except OSError as e:									# If an error occurred, I use the OSError output to tell me what went wrong.
        print(f"{burnt_bridges} was too damp! The match said: {e}")				# Were the matches damp? No more powder? Or was it user error, as I experienced?
 
												# Disclaimer: I spent a while researching how to delete directories like this,
												# so this might be bad in in a real-world scenario. I could have typed os.rmdir over
												# and over, but I wanted to see if there was a cooler way to do it. Also, that would
												# have been really annoying to type out over and over again.