__author__ = 'dongfeng'
import os
os.chdir('C:\Test')
with open('Yr20060504_ascii.txt') as infile, open('rainfall_SUB30_Yr20060504_ascii.txt', 'w') as outfile:
    #open files
    for line in infile:
        #loop in lines
         if line.startswith(("SUB30")):
            #detect the requirement
            outfile.write(line)