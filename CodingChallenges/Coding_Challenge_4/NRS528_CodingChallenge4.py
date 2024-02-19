# Filename: NRS528_CodingChallenge4.py
# Author: Elliot Vosburgh
# Date: 18 February 2024
# Description:
#
#	This file contains my answers to Coding Challenge 4.

'''
NOTE: Lines 9-39 generate a shapefile for you to use. I could've included a shapefile, but I learned
      a lot by creating one with arcpy. The shapefile is stored in the directory you are running this
      Python file from. If this isn't what you wanted from the assignment let me know and I can do it
      in a different way.
'''

import os
import arcpy

# Setup for creating the shapefile

your_path = os.path.dirname(os.path.realpath(__file__))                                 # Find the current directory
shp_name = "cc4_points.shp"                                                             # Name the new shapefile
geom_type = "POINT"                                                                     # It'll be a point feature class

# Define new shapefile to make amending it convenient

new_shape_file = arcpy.CreateFeatureclass_management(your_path, shp_name, geom_type, spatial_reference=4326)    # 4326 is WGS1984. I have the code for RI State Plane
                                                                                                                # U.S. ft but Python didn't like the foot coordinates
                                                                                                                # I was giving it in fc_points.

# "Prudence, Patience, Hope, and Despair. And Little Hog Island over there." ~ Roger Williams
# Define the coordinates for each island referenced in the rhyme

fc_points = [
    [-71.359466, 41.657013],
    [-71.367339, 41.602287],
    [-71.361238, 41.607873],
    [-71.316181, 41.610629],
    [-71.281009, 41.641571]
]

for i in fc_points:	            # I didn't know if this was required or not. It seems like arcpy
    for j in range(len(i)):     # automatically converts coordinate values to floats,as it did in
        i[j] = float(i[j])      # my initial testing, but I've included this loop anyway.
        
# This is what I will showcase: the InsertCursor class of the Data Access module (arcpy.da)

with arcpy.da.InsertCursor(new_shape_file, ['SHAPE@XY']) as cursor:     # Making it easier to read...

    for point in fc_points:         # For each [X,Y] nested list in fc_points,
        cursor.insertRow(point)     # insert a row at coordinates X, Y in the
                                    # feature class table.

'''
InsertCursor is a very useful Data Access class, allowing for the addition of new rows to
tables. 

SHAPE@XY is a tuple. You said at the beginning of the course that we would not useful tuples,
but by their nature they seem essential to vector data like in this example. Coordinates have
a fixed number of values. In this case, just X and Y. InsertCursor allows for XYZ as well.

By storing coordinates in tuples, their order and values are immutable. 
'''