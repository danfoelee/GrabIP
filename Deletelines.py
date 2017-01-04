__author__ = 'dongfeng'
import os
os.chdir('C:\Test')
with open('boo1.txt') as infile, open('tempboo1.txt', 'w') as outfile:
    #open files
    for line in infile:
        #loop in lines
        if len(line.strip()) > 1:
            #detect the requirement
            outfile.write(line)