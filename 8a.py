def Highest_marks(marks,names):
    if(len(marks)!=len(names)):
        return ("Mismatch in records ....Get out")
    
    res=[]
    max_mark = max(marks)
    for i in range(len(names)):
        if marks[i]==max_mark:
            res.append(tuple((names[i],marks[i])))

    return res


#Take input from user in exam
x=[90,70,45,90]
y=['a','b','c','d']
print(Highest_marks(x,y))
