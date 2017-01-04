__author__ = 'dongfeng'
# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "E:\Projects\TRWD\Urban\Python_work"

# Set local variables
i = 10
inTable = "sub{}_raster".format(i)
fieldName = "urbanP"
expression = "geturbanP(int(!LUCODE!))"
codeblock = """def geturbanP(land):
    if land == 111 or land == 142:
        return 80
    elif land == 112 or land == 122 or land == 124 or land == 131 or land == 145 or land == 147 or land == 160:
        return 95
    elif land == 113 or land == 144:
        return 40
    elif land == 114 or land == 143:
        return 70
    elif land == 121:
        return 90
    elif land == 123:
        return 50
    elif land == 141:
        return 30
    elif land == 146 or land == 306 or land == 308 or land == 500:
        return 100
    elif land == 171 or land == 172:
        return 10
    elif land == 173:
        return 20
    else:
        return 0"""

# Execute AddField
arcpy.AddField_management(inTable, fieldName, "FLOAT")

# Execute CalculateField
arcpy.CalculateField_management(inTable, fieldName, expression, "PYTHON_9.3", codeblock)

