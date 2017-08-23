#!/usr/bin/python
counter=0
total=sum(1 for line in open("/files/text1.txt"))
file1_total=total

with open("/files/text1.txt","r") as text:

    lines=text.readlines()

    n1=lines[file1_total-1]
    #print(n1)

    a1=(n1[-10:])

total1=sum(1 for line in open("/files/text1.txt"))
file2_total=total1

with open("/files/text2.txt","r") as text1:
    lines1=text1.readlines()

    n2=lines1[file2_total-1]

    a2=(n2[-10:])


if a1==a2:

    while counter<total:
        #print("hai")
        with open("/files/output.txt","a") as z:


            for tot in lines[counter]:

                z.write(tot)
            z.write(",")

            for tot1 in lines1[counter]:
                z.write(tot1)
    counter=counter+1
                

else:
     print("no match")
