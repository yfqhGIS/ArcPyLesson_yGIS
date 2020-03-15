import arcpy

shpPath="C:\Users\qin\Desktop\data27\west.shp"

searchCursor=arcpy.da.SearchCursor(shpPath,["SHAPE@"])
insertCursor=arcpy.da.InsertCursor(shpPath,["SHAPE@"])

for row in searchCursor:
    ext=row[0]

    yMid=(ext.extent.YMin+ext.extent.YMax)/2
    xMid=(ext.extent.XMin+ext.extent.XMax)/2

    #points=arcpy.Array(([arcpy.Point(ext.extent.XMin,yMid),arcpy.Point(ext.extent.XMax,yMid)]))
    points = arcpy.Array(([arcpy.Point(xMid, ext.extent.YMin), arcpy.Point(xMid, ext.extent.YMax)]))
    polyline=arcpy.Polyline(points)
    geometries=ext.cut(polyline)

    insertCursor.insertRow([geometries[1]])
    insertCursor.insertRow([geometries[0]])
arcpy.AddMessage("finished")
