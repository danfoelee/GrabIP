import os
os.chdir('C:\Test')
        #changeTp
with open('100_year_losses.txt') as infile, open('temp100_year_losses.txt', 'w') as outfile:
        #open files
    for line in infile:
        #loop in lines
        if line.startswith(("     Snyde")):
            #detect the requirement
            a = line
            #read content in line
            b = a.split()
            #split the string
            c = float(b[2])
            #read the Tp number
            c = c*(0.75+i*0.05)
            #process the Tp
            d = str(c)
            #return the Tp as string
            outfile.write('     SnyderTp: wo ri le ni ma ' )
            #write the new result
        else: outfile.write(line)