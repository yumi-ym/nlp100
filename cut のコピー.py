import sys
f1 = open("col1.txt","w")
f2 = open("col2.txt","w")

for line in sys.stdin.readlines():
    line=line.rstrip("\n\r")
    columns = line.split("\t")
   
    f1.write(columns[0]+"\n")
    f2.write(columns[1]+"\n")
   
f1.close()  
f2.close()
    







