import arcpy
import os
from arcpy import env

os.chdir("E:\Projects\TRWD\Urban\Python_work")
env.workspace = "E:\Projects\TRWD\Urban\Python_work"
arcpy.MakeFeatureLayer_management("area_westfok.shp", "lyr")
arcpy.TabletoTable_conversion()