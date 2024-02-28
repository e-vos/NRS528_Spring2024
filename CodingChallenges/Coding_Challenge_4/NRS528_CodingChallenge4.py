# Filename: NRS528_CodingChallenge4.py
# Author: Elliot Vosburgh
# Date: 18 February 2024
# Description:
#
#	This file contains my answers to Coding Challenge 4.

# from arcpy import env
# from arcpy.sa import *
import os
import arcpy

your_path = os.path.dirname(os.path.realpath(__file__))  # Your current directory

shp_name = "points.shp"

# Need to add "population" field, else kernel density won't work
new_field_name = "Population"

arcpy.AddField_management(shp_name, new_field_name, "DOUBLE")

with arcpy.da.UpdateCursor(shp_name, new_field_name) as cursor:

    for row in cursor:

        row[0] = 1
        cursor.updateRow(row)

population_field = new_field_name

env.workspace = your_path

# Create a feature layer from the input shapefile
input_layer = "input_layer"
arcpy.MakeFeatureLayer_management(shp_name, input_layer)


# Perform kernel density calculation
outKDens = KernelDensity(input_layer, population_field, 45, 1200, "SQUARE_MILES", "", "GEODESIC")

# Save as kdens.tif in the same directory
save_path = os.path.join(your_path, "kdens.tif")
outKDens.save(save_path)