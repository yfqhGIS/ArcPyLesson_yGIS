#coding:utf-8
import os
import arcpy



def clipTest(shpPath,raster,resultFolder):
  with arcpy.da.SearchCursor(shpPath,["NAME","SHAPE@"]) as cursor:
    for row in cursor:
        mask=row[1]
        strJX=str(mask.extent.XMin)+" "+str(mask.extent.YMin)+" "
        strJX=strJX+str(mask.extent.XMax)+" "+str(mask.extent.YMax)
        outpath=os.path.join(resultFolder, str(row[0].encode("utf-8")) + ".img")
        arcpy.Clip_management(raster,strJX,outpath,mask,"0","ClippingGeometry")

shpPath="C:\Users\qin\Desktop\ArcLesson25\west.shp"
raster="C:\\Users\\qin\\Desktop\\ArcLesson25\\1.TIF"
resultFolder="C:\Users\qin\Desktop\ArcLesson25"
clipTest(shpPath,raster,resultFolder)
