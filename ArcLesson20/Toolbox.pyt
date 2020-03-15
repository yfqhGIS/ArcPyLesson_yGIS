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
        self.label = "读取shp字段写入到txt文件"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        shpPath=arcpy.Parameter({})
        shpPath.name="shpPath"
        shpPath.datatype="GPFeatureLayer"
        shpPath.direction="Input"
        shpPath.displayName="shp文件"
        shpPath.parameterType="Required"

        field=arcpy.Parameter({})
        field.name="field"
        field.datatype="Field"
        field.direction="Input"
        field.displayName="字段名称"
        field.parameterType="Required"

        field.parameterDependencies=[shpPath.name]

        txtPath=arcpy.Parameter({})
        txtPath.name="txtPath"
        txtPath.datatype="DETextfile"
        txtPath.direction="Output"
        txtPath.displayName="txt文件"
        txtPath.parameterType="Required"
        params = [shpPath,field,txtPath]
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
        shpPath=parameters[0].valueAsText
        field=parameters[1].valueAsText
        txtPath=parameters[2].valueAsText
        from demo import writeFieldToTXT
        writeFieldToTXT(shpPath,field,txtPath)
        return
