import os
import arcpy

arcpy.env.overwriteOutput = True

your_path = os.path.dirname(os.path.realpath(__file__))
shp_name = "cc4_points.shp"
geom_type = "POINT"

new_shape_file = arcpy.CreateFeatureclass_management(your_path, shp_name, geom_type, spatial_reference=4326)

fc_points = [
    [-71.359466, 41.657013],
    [-71.367339, 41.602287],
    [-71.361238, 41.607873],
    [-71.316181, 41.610629],
    [-71.281009, 41.641571]
]

for i in fc_points:
    for j in range(len(i)):
        i[j] = float(i[j])

with arcpy.da.InsertCursor(new_shape_file, ['SHAPE@XY']) as insert_cursor:
    for point in fc_points:
        insert_cursor.insertRow([point])