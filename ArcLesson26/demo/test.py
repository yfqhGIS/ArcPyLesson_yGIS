#coding:utf-8
import arcpy



def testraster(workspace,raster_type,coor_system):
    arcpy.env.workspace=workspace
    rasterlist = arcpy.ListRasters("*", raster_type)
    for data in rasterlist:
        arcpy.DefineProjection_management(in_dataset=data,coor_system=coor_system)
    arcpy.AddMessage("finished")


