#encoding:gbk
import arcpy

# root=r"C:\Users\qin\Desktop\test\shp\within"
# shpPath=r"C:\Users\qin\Desktop\test\shp\within\New_Shapefile.shp"

shpPath=arcpy.GetParameterAsText(0)
txtPath=arcpy.GetParameterAsText(1)

def getFirtAndLastPt(file,txtpath):
  #txtPrx="\\result.txt"
  with open(txtpath,"w") as f:
    with arcpy.da.SearchCursor(file,["FID","SHAPE@"]) as cursor:
      for row in cursor:
        shape=row[1]
        fid=row[0]

        firstPt=shape.firstPoint
        lastPt=shape.lastPoint
        strResult=str(fid)+","+str(firstPt.X)+","+str(firstPt.Y)+","+str(lastPt.X)+","+str(lastPt.Y)+"\n"
        f.write(strResult)

    arcpy.AddMessage("finished")

getFirtAndLastPt(shpPath,txtPath)




