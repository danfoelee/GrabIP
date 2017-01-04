__author__ = 'dongfeng'
# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "E:\Projects\TRWD\Urban\Python_work"

# Set local variables
arcpy.MakeFeatureLayer_management("WestFork.shp", "lyr")
arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", """ "LOCATION" = 'SUB30' """)
in_features = ["lyr","Landuse_WestFork.shp"]
intersectOutput  = "Landuse_WF"
# Execute Clip
arcpy.Intersect_analysis(in_features, intersectOutput)
# add urbanization percentage
arcpy.AddField_management("Landuse_WF", "Urban", "FLOAT",)
