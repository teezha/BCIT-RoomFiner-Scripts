import arcpy

room_points = arcpy.GetParameterAsText(0)
output_lines = arcpy.GetParameterAsText(1)

fields = ['xcoord', 'ycoord', 'NEAR_X', 'NEAR_Y']
point = arcpy.Point()
array = arcpy.Array()

featureList = []
output = arcpy.InsertCursor(output_lines)
new_row = output.newRow()

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
        new_row.shape = polyline
        output.insertRow(new_row)
    del new_row
    del output
