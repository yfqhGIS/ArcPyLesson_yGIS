#coding:gbk
import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "批量定义投影"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        coor_system = arcpy.Parameter({})
        coor_system.displayName = "空间参考"
        coor_system.name = "coor_system"
        coor_system.datatype = "GPSpatialReference"
        coor_system.direction = "Input"
        coor_system.parameterType = "Required"

        raster_type=arcpy.Parameter({})
        raster_type.displayName = "数据格式"
        raster_type.name = "raster_type"
        raster_type.datatype = "GPString"
        raster_type.direction = "Input"
        raster_type.parameterType = "Required"

        raster_type.filter.type = "ValueList"
        raster_type.filter.list = ["TIF", "IMG", "TIFF", "GRID"]
        raster_type.defaultEnvironmentName = "TIF"
        raster_type.value = "TIF"

        workspace = arcpy.Parameter({})
        workspace.displayName = "数据集文件夹"
        workspace.name = "workspace"
        workspace.datatype = "DEWorkspace"
        workspace.direction = "Input"
        workspace.parameterType = "Required"

        params = [workspace,coor_system,raster_type]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        workspace=parameters[0].valueAsText
        coor_system=parameters[1].valueAsText
        raster_type=parameters[2].valueAsText
        from test import testraster
        testraster(workspace,raster_type,coor_system)
        return
