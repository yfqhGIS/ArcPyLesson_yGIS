#encoding:utf-8
import arcpy

def writeFieldToTXT(shpPath,field,txtPath):
    with open(txtPath,"w") as f:
        with arcpy.da.SearchCursor(shpPath, [field]) as cursor:
            for row in cursor:
                fieldValue=row[0]
                strValue=str(fieldValue)+"\n"
                f.write(strValue)
        arcpy.AddMessage("finished")
        print "finished"

root=r"C:\Users\qin\Desktop\test\shp\within"
shpPath=r"C:\Users\qin\Desktop\test\shp\within\New_Shapefile.shp"
txtPath=root+"\\result2.txt"

#writeFieldToTXT(shpPath,"FID",txtPath)