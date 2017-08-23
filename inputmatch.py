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

    with open("/files/output.txt","w") as z:

        for tot in lines[0]:

            z.write(tot)
        z.write(",")

        for tot1 in lines1[0]:
            z.write(tot1)

        for tot2 in lines[1]:
            z.write(tot2)

        z.write(",")

        for tot3 in lines1[1]:
            z.write(tot3)
            
              
                

else:
     print("no match")
