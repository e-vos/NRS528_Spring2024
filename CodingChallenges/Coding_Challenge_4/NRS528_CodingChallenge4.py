# Filename: NRS528_CodingChallenge4.py
# Author: Elliot Vosburgh
# Date: 18 February 2024
# Description:
#
#	This file contains my answers to Coding Challenge 4.
#
#   In the first part I create an example shapefile for use in this exercise. It's a point feature class
#       that contains five objects corresponding to five islands in Narragansett Bay.
#
#   In the second part, I showcase a tool called Create Thiessen Polygons by applying it to the example
#       dataset.
#
#   I also make a comment on tuples that occurred to me when I was working on this assignment.


import os
import arcpy

#########################
# I. Create example data
#########################

your_path = os.path.dirname(os.path.realpath(__file__))                                 # Find the current directory
shp_name = "cc4_points.shp"                                                             # Name the new shapefile
geom_type = "POINT"                                                                     # It'll be a point feature class

# Define new shapefile to make amending it convenient

new_shape_file = arcpy.CreateFeatureclass_management(your_path, shp_name, geom_type, spatial_reference=4326)    # 4326 is WGS1984. I have the code for RI State Plane
                                                                                                                # U.S. ft but Python didn't like the foot coordinates
                                                                                                                # I was giving it in fc_points.

# "Prudence, Patience, Hope, and Despair. And Little Hog Island over there." ~ Colonial nursery rhyme
# Define the coordinates for each island referenced in the rhyme

fc_points = [
    [-71.359466, 41.657013],
    [-71.367339, 41.602287],
    [-71.361238, 41.607873],
    [-71.316181, 41.610629],
    [-71.281009, 41.641571]
]

for i in fc_points:	            # I didn't know if this was required or not. It seems like arcpy
    for j in range(len(i)):     # automatically converts coordinate values to floats, as it did in
        i[j] = float(i[j])      # my initial testing, but I've included this loop anyway.

with arcpy.da.InsertCursor(new_shape_file, ['SHAPE@XY']) as cursor:     # Making it easier to read...

    for point in fc_points:         # For each [X,Y] nested list in fc_points,
        cursor.insertRow(point)     # insert a row at coordinates X, Y in the
                                    # feature class table.

'''
InsertCursor is a very useful Data Access class, allowing for the addition of new rows to
tables. 

SHAPE@XY is a tuple. You said at the beginning of the course that we would not use tuples,
but by their nature they seem essential to vector data like in this example.yB storing 
coordinates in tuples, their order and values are immutable. 
'''

#############################################
# II. Tool showcase: Create Thiessen Polygons
#############################################

outFeatureClass = "thiessen_polys.shp"
out_shp = arcpy.CreateFeatureclass_management(your_path, outFeatureClass, "POLYGON", spatial_reference=4326)	# Again
outFields = "ALL"

arcpy.analysis.CreateThiessenPolygons(shp_name, out_shp, outFields)	    # Use Create Thiessen Polygons on points to generate
                                                                        # Thiessen polygons corresponding to fc_points. From what
                                                                        # I learned about them, this little example has no
                                                                        # meaning. It just looks cool. I won't pretend to
                                                                        # understand how they're calculated mathematically.