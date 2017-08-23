#!/usr/bin/python
import re
from os.path import normpath, basename


with open("/awsboto/inputfile1.txt","rw") as text1:

    for aa in text1.readlines():

        last_line1=aa[-1]   

with open("/awsboto/inputfile2.txt","rw") as text2:


    for bb in text2.readlines():

    
        last_line2=bb[-1]

if last_line1==last_line2:

    with open("/awsboto/inputfile1.txt") as a:

        lines=a.readlines()
        n1=lines[0]
        n2=lines[1]
    
    
    with open("/awsboto/inputfile2.txt") as d:

        lines1=d.readlines()
        n3=lines1[0]
        n4=lines1[1]

    with open ("/awsboto/outputfile.txt","a") as b:
        for tot in n1:
            b.write(tot)
            

        for tot2 in n3:
            b.write(tot2)            

        for tot3 in n2:
            b.write(tot3)

        for tot4 in n4:
            b.write(tot4)

else:

    print("no match")
