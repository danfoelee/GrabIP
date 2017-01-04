__author__ = 'dongfeng'
import os
import subprocess
import shutil


i=0
while (i<11):
        os.chdir('C:\Test')
        #changeTp
        with open('100_year_losses.txt') as infile, open('temp100_year_losses.txt', 'w') as outfile:
        #open files
            for line in infile:
        #loop in lines
                if line.startswith(("     SnyderTp")):
            #detect the requirement
                    a = line
            #read content in line
                    b = a.split()
            #split the string
                    c = float(b[1])
            #read the Tp number
                    c = c*(0.75+i*0.05)
            #process the Tp
                    d = str(c)
            #return the Tp as string
                    outfile.write('     SnyderTp: ' + d + '\n')
            #write the new result
                else: outfile.write(line)
        with open ('compute.txt') as infile, open('tempcompute.txt', 'w') as outfile:
        #open files
            for line in infile:
            #loop in lines
                 if line.startswith(("Compute")):
                    outfile.write('Compute("'+str(i)+ '")'+ '\n')
            #write the new result
                 else: outfile.write(line)
        with open('UT2012FutureMP_DS.txt') as infile, open('tempUT2012FutureMP_DS.txt', 'w') as outfile:
        #open files
            for line in infile:
         #loop in lines
                if line.startswith(("Run")):
                    outfile.write('Run:'+str(i)+ '\n')
            #write the new result
                else: outfile.write(line)
        shutil.copy('temp100_year_losses.txt','C:\TWRD_HMS\Pythoncontrolmodle\UT2012FutureMP_DS')
        shutil.copy('tempcompute.txt','C:\TWRD_HMS\Pythoncontrolmodle\UT2012FutureMP_DS')
        shutil.copy('tempUT2012FutureMP_DS.txt','C:\TWRD_HMS\Pythoncontrolmodle\UT2012FutureMP_DS')
        os.chdir('C:\TWRD_HMS\Pythoncontrolmodle\UT2012FutureMP_DS')
        os.rename('temp100_year_losses.txt','100_year_losses.basin')
        os.rename('tempcompute.txt','compute.script')
        os.rename('tempUT2012FutureMP_DS.txt','UT2012FutureMP_DS.run')
        os.system("C:\Test\hms.bat")
        os.remove('100_year_losses.basin')
        os.remove('compute.script')
        os.remove('UT2012FutureMP_DS.run')
        i = i + 1

 # os.chdir (c'
 # os.chdir('C:\Python27')
 #  shutil.copy('new100_year_losses.basin', 'C:\TWRD_HMS\Pythoncontrolmodle\UT2012FutureMP_DS')
 #   os.rename('C:\TWRD_HMS\Pythoncontrolmodle\UT2012FutureMP_DS\new100_year_losses.basin','C:\TWRD_HMS\Pythoncontrolmodle\UT2012FutureMP_DS\100_year_losses.basin')




#os. system("C:\Python27\hms.bat")


