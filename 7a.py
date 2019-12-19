A={}
n=int(input("Enter the number of records: "))
print("Enter Student SRN,P_MARKS,C_MARKS,M_MARKS,B_MARKS in order ")
for i in range(n):
    inp = input().split()
    A[inp[0]] = [int(inp[1]),int(inp[2]),int(inp[3]),int(inp[4])]

print()


Marks={}
for i in A:
    Marks[i]=sum(A[i])
for i,j in sorted(Marks.items(), key=lambda a: a[1]):
    print(i,"==>",j)

#name of students with same marks 
M_marks=[x[2] for x in A.values()]
student_details={}
for i in M_marks:
    student_details[i]=[]
    for j in A:
        if(i==A[j][2]):
            student_details[i].append(j)
print(student_details)
