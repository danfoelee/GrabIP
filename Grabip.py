__author__ = 'dongfeng'
import socket
import os
os.chdir('C:\Users\dongfeng\Desktop')
s = socket.gethostbyname(socket.gethostname())
with open('ip.txt', 'w') as outfile:
    outfile.write(s)
outfile.close()