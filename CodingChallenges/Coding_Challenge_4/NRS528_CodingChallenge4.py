# Filename: NRS528_CodingChallenge4.py
# Author: Elliot Vosburgh
# Date: 18 February 2024
# Description:
#
#	This file contains my answers to Coding Challenge 4.

import os
import arcpy

# Setup for creating the shapefile

your_path = os.path.dirname(os.path.realpath(__file__))                                 # Find the current directory
shp_name = "cc4_points.shp"                                                             # Name the new shapefile
geom_type = "POINT"                                                                     # Point feature class

# Define new shapefile to make amending it convenient

new_shape_file = arcpy.CreateFeatureclass_management(your_path, shp_name, geom_type, spatial_reference=4326)

# "Prudence, Patience, Hope, and Despair. And Little Hog Island over there." ~ Roger Williams

# Define the coordinates for each island referenced in the rhyme

fc_points = [
    [-71.359466, 41.657013],
    [-71.367339, 41.602287],
    [-71.361238, 41.607873],
    [-71.316181, 41.610629],
    [-71.281009, 41.641571]
]

for i in fc_points:		# I didn't know if this was required or not.
    for j in range(len(i)):	# It seems like arcpy 
        i[j] = float(i[j])