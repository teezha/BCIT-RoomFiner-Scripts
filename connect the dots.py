import os

import arcpy

# script tool parameters
room_points = arcpy.GetParameterAsText(0)
output_lines = arcpy.GetParameterAsText(1)
# sets the fields to look through
fields = ['xcoord', 'ycoord', 'NEAR_X', 'NEAR_Y']
point = arcpy.Point()
array = arcpy.Array()
# Splits the file paths
drive, path_file = os.path.split(output_lines)
path, filename = os.path.split(path_file)
# Reformats the file names again to paths
outpath = drive + "\\" + path
outfile = outpath + "\\" + filename
# Create Spatial ref
spatial_ref = arcpy.Describe(room_points).spatialReference
# Overwrites previous attemps
try:
    arcpy.CreateFeatureclass_management(outpath, filename, "POLYLINE", "", "", "", spatial_ref)

except arcpy.ExecuteError:
    arcpy.AddWarning("File: " + outfile + " already exists! Overwriting now!")
    if arcpy.Exists(outfile):
        arcpy.Delete_management(outfile)
        arcpy.CreateFeatureclass_management(outpath, filename, "POLYLINE", "", "", "", spatial_ref)

featureList = []
output = arcpy.InsertCursor(output_lines)
new_row = output.newRow()

# actual creation
with arcpy.da.SearchCursor(room_points, fields) as cursor:
    for row in cursor:
        # set and add the X and Y for the event point and the line points (calculated from NEAR)
        point.X = row[0]
        point.Y = row[1]
        array.add(point)
        point.X = row[2]
        point.Y = row[3]
        array.add(point)
        # Creates a polyline between the two points
        polyline = arcpy.Polyline(array)
        # Clear array
        array.removeAll()
        # Appends the list to the object
        featureList.append(polyline)
        # Inserts the feature made
        new_row.shape = polyline
        output.insertRow(new_row)
    del new_row
    del output
