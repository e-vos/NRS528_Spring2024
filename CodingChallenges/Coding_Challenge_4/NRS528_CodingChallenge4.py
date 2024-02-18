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
spat_ref = arcpy.SpatialReference("NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet")    # RI State Plane (ft)

arcpy.env.workspace = your_path                                                         # Define workspace
arcpy.management.CreateFeatureclass(your_path, shp_name, geom_type, spat_ref)           # Create the feature class

# "Prudence, Patience, Hope, and Despair. And Little Hog Island over there." ~ Roger Williams

fc_points = [[41.657013, -71.359466],[41.602287, -71.367339],[41.607873, -71.361238],[41.610629, -71.316181],[41.641571, -71.281009]]   # Define the coordinates for
# pt = arcpy.Point()                                                                                                                    # the islands in the rhyme
ptGeoms = []            # Initialize list to contain point geometries

# 
for p in fc_points:     # Iterate through fc_points and define X and Y coordinates by index
    # pt.X = p[0]
    # pt.Y = p[1]
    pt = arcpy.Point(p[0], p[1])
    ptGeoms.append(arcpy.PointGeometry(pt))

arcpy.CopyFeatures_management(ptGeoms, os.path.join(your_path, shp_name))       # Add ptGeoms to the feature class