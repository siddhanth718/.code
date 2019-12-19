f1=open("9a.txt",'r')
f2=open("9aOutput.txt",'w')
for i,j in enumerate(f1.readlines(),1):
        f2.write(str(i)+" "+j)

f1.close()
f2.close()
