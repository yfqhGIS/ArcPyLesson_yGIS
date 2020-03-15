import arcpy
wildcard='*{0}*{1}*'.format("19","5")
arcpy.env.workspace = 'C:\Users\qin\Desktop\ArcLesson28\.idea'
lfc1=arcpy.ListFeatureClasses(wildcard, "Polygon")
lfc=list(set(arcpy.ListFeatureClasses("*data.shp", "Polygon")) |
                 set(arcpy.ListFeatureClasses("f*", "Point")))
x=0
