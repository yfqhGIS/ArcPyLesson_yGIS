#coding:utf-8
import arcpy

shpPath=r"C:\Users\qin\Desktop\lesson30data\test\polyline.shp"
sp=arcpy.Describe(shpPath).spatialReference
cursor=arcpy.da.SearchCursor(shpPath,["FID","SHAPE@","SHAPE@LENGTH"])
for row in cursor:
    fid=row[0]
    geometry=row[1]
    length=row[2]
    CNT=int(length/2)

    createPolyline = r"in_memory\tempPolyline"
    arcpy.CreateFeatureclass_management(
        "in_memory",
        "tempPolyline",
        "POLYLINE", "", "", "",
        sp)

    curPolyline=arcpy.InsertCursor(createPolyline)
    curRowPolyline=curPolyline.newRow()
    curRowPolyline.shape=geometry
    curPolyline.insertRow(curRowPolyline)

    createPoint = r"in_memory\tempPoint"
    arcpy.CreateFeatureclass_management(
        "in_memory",
        "tempPoint",
        "POINT", "", "", "",
        sp)

    for index in range(CNT):
        point=geometry.positionAlongLine((index+1)*2,False)
        curPoint = arcpy.InsertCursor(createPoint)
        newRowPoint = curPoint.newRow()
        newRowPoint.shape = point
        curPoint.insertRow(newRowPoint)

    arcpy.SplitLineAtPoint_management(in_features="in_memory/tempPolyline", point_features="in_memory/tempPoint",
                                      out_feature_class="C:/Users/qin/Desktop/lesson30data/test/"+str(fid)+".shp",
                                      search_radius="1 Meters")

    arcpy.Delete_management("in_memory")



