__author__ = 'dongfeng'
import arcpy
import os
from arcpy import env
os.chdir('E:\Projects\TRWD\Urban\Python_work')
# Set workspace
env.workspace = "E:\Projects\TRWD\Urban\Python_work"

arcpy.MakeFeatureLayer_management("Landuse_WF2055_intersected.shp", "lyr")

i = 14
for i in range(14,42):
    Name = 'SUB'+str(i)

    where =  '"LOCATION" = ' + "'%s'" %Name

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", where)

# Write the selected features to a new featureclass
    arcpy.CopyFeatures_management("lyr", "SUB{}_Landuse2055".format(i))

    arcpy.FeatureToRaster_conversion("SUB{}_Landuse2055.shp".format(i), "LUCODE", "SUB{}2055_R".format(i))

    inTable = "SUB{}2055_R".format(i)
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


    fieldName = "total"
    expression = "!COUNT!*!URBANP!"

# Execute AddField
    arcpy.AddField_management(inTable, fieldName, "FLOAT")

# Execute CalculateField
    arcpy.CalculateField_management(inTable, fieldName, expression, "PYTHON_9.3")

    out_table = "stats{}2055.txt".format(i)
    arcpy.Statistics_analysis (inTable, out_table, [["COUNT","SUM"],["TOTAl","SUM"]])

    text_file = open("stats{}2055.txt".format(i),"r")
    lines = text_file.read().split(',')
    Percen = float(lines[6])/float(lines[5])
    result_file = open("stats_result2055.txt","a")
    result_file.write('SUB'+ str(i) +'    ' + str(Percen)+'\n')
    text_file.close()
    result_file.close()


