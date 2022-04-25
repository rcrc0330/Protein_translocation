import sys
first=open("first.txt","r").read()
second=open("second.txt","r").read()
third=open("third.txt","r").read()
forth=open("forth.txt","r").read()
fifth=open("fifth.txt","r").read()
veloseed=sys.argv[1]
file=open("protein_run/protein_run" + veloseed + ".in","w")
data=first+veloseed+second+str(int(veloseed)*54321)+third+str(int(veloseed)*12345)+forth+veloseed+fifth
file.write(data)