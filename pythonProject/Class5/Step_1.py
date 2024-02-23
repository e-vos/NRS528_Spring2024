#####
# Step 1 - Executing and reporting tool outputs
#####

# Part a - convert CSV to shapefile

# Help on Tool: http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/make-xy-event-layer.htm.
# Using the data Step_1_Lionfish.csv, we will use arcpy to convert this to a shapefile.
#
# import arcpy
# # Set your workspace to the directory where you are storing your files
# arcpy.env.workspace = r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\pythonProject\Class5"
# # arcpy.env.OverwriteOutput = True
#
# in_Table = r"Step_1_Lionfish.csv"
# x_coords = "X"
# y_coords = "Y"
# z_coords = ""
# out_Layer = "lionfish"
# saved_Layer = r"Step_1_Lionfish_Output.shp"
#
# # Set the spatial reference
# spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
#
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#
# # Print the total rows
# print(arcpy.GetCount_management(lyr))
#
# # Save to a layer file
# arcpy.CopyFeatures_management(lyr, saved_Layer)
#
# if arcpy.Exists(saved_Layer):
#     print("Created file successfully!")


# Tasks - Using the file provided "Step_1_Deep_Coral.csv", undertake the following: Hint: spatial
# reference is the same as above, i.e. WGS 1984.

##### 1. Convert the file to a shapefile.
import arcpy
import os

arcpy.env.workspace = os.path.dirname(os.path.realpath(__file__))
arcpy.env.overwriteOutput = True

inTable = r"Step_1_Deep_Coral.csv"
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
z_coords = ""
out_Layer = "deepcoral"
saved_Layer = r"Step_2_Deep_Coral_Output.shp"

spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(inTable, x_coords, y_coords, out_Layer, spRef, z_coords)

print(arcpy.GetCount_management(lyr))

arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

spatialRef = arcpy.Describe(out_Layer).SpatialReference
print(spatialRef.name)

##### 2. Print the count of the number of records in the file. (Hint: see above!)
# https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-count.htm

##### 3. Check the correct coordinate system has been applied (Hint: see last week!)

##### 4. Visualize the file in ArcPro by dragging it into the program.

