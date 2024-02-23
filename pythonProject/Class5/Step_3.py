#####
# Step 3 - Executing multiple tools - and automating most of it
#####

# We will use the exact same approach to generate a heatmap from a CSV file, but this time
# You will have to automate the extraction of start extent, opposite corner etc for the fishnet
# generation. I have given hints, but everything you are using here has been shown in last week's
# and this week's session.

# Using Step_3_Cepphus_grylle.csv:

# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.

# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degrees.

# 4. Undertake a Spatial Join to join the fishnet to the observed points.

# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
# arcpy.Delete_management()..

# 6. Visualize in ArcGIS Pro

# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
# import arcpy
# arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open in
# ArcGIS Pro or an other program such as Excel.

import arcpy
import os

arcpy.env.workspace = os.path.dirname(os.path.realpath(__file__))
print(f"The workspace is set to {arcpy.env.workspace}")

arcpy.env.overwriteOutput = True

inTable = r"Step_3_Cepphus_grylle.csv"
x_coords = "lon"
y_coords = "lat"
outLayer = "grylle"
savedLayer = r"grylle_output.shp"
spRef = arcpy.SpatialReference(4326)

lyr = arcpy.MakeXYEventLayer_management(inTable, x_coords, y_coords, outLayer, spRef, "")

print(f"Attempting to copy features from {lyr} to {savedLayer}")
arcpy.CopyFeatures_management(lyr, savedLayer)
print(f"Attempt successful: copied {lyr} to {savedLayer}")

if arcpy.Exists(savedLayer):
    print(f"Checking if {savedLayer} exists...")
    print(f"Created file {savedLayer} successfully!")

# Extract minimum and maximum coordinate values for savedLayer

desc = arcpy.Describe(savedLayer)   # Shorthand
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax

print(f"Coordinates information:\nXMin = {XMin}, XMax = {XMax}, YMin = {YMin}, YMax = {YMax}")

# Fishnet generation for heatmap

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326) # Set spatial reference equal to the output coordinate system

outFC = "Step_3_Fishnet.shp"

print(f"Setting output feature class for fishnet as {outFC} projected in {arcpy.env.outputCoordinateSystem.name}...\nSuccessful!")

originC = str(XMin) + " " + str(YMin)
yAxisC = str(XMin) + " " + str(YMin + 1)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""
numCols = ""
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

print(f"Setting origin coordinate at {originC} with a y-axis coordinate at {yAxisC}\nCell size of {cellSizeWidth} wide and {cellSizeHeight} high with geometry {geometryType}...")

print(f"Attempting to create fishnet polygon called {outFC}...")
arcpy.CreateFishnet_management(outFC, originC, yAxisC,
                               cellSizeWidth, cellSizeHeight, numRows, numCols,
                               oppositeCorner, labels, templateExtent, geometryType)
print(f"Successfully created {outFC} feature class!")

# Perform spatial join

target_features="Step_3_Fishnet.shp"
join_features="grylle_output.shp"
out_feature_class="grylle_heatmap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

print(f"Attempting to perform spatial join on {target_features} with {join_features}...")
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
print(f"Successfully created {out_feature_class} from spatial join!")

print(f"Attempting to delete intermediaries...")
arcpy.management.Delete(savedLayer)
arcpy.management.Delete(outFC)
print(f"Successfully deleted {savedLayer} and {outFC} from the working directory!")