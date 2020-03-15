import  arcpy

shpPath=r"C:\Users\qin\Desktop\ArcLesson\data31\test.shp"
with arcpy.da.SearchCursor(shpPath,["SHAPE@","FID"]) as cursor:
    for row in cursor:
        geometry=row[0]
        for parts in geometry:
            length=len(parts)
            for index in range(length-1):
                ptStart=parts[index]
                ptEnd=parts[index+1]
                dx=ptStart.X-ptEnd.X
                dy=ptStart.Y-ptEnd.Y
                xxyy=pow(dx,2)+pow(dy,2)
                distance=pow(xxyy,0.5)
                print distance