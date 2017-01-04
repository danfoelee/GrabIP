
def  change(i):
    import os
    os.chdir('C:\Test')
    with open('compute.txt') as infile, open('tempcompute.txt', 'w') as outfile:
        #open files
        for line in infile:
         #loop in lines
             if line.startswith(("Compute")):
                outfile.write('Compute("'+str(i)+ '")'+ '\n')
            #write the new result
             else: outfile.write(line)
        # just return the original string

