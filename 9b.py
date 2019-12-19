print("-----------------------UNION-------------------------------")
with open('a.txt','r') as f1,open('b.txt','r') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            print(i.strip())        
        else:
            print(i.strip(),j.strip())
print("---------------------INTERSECTION--------------------------")
with open('a.txt') as f1,open('b.txt') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            print(i.strip())

print("--------------------(set1 - set2)--------------------------")
with open('a.txt') as f1,open('b.txt') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            pass
        else:
            print(i.strip())
            
print("---------------------SYMMETRIC DIFFERENCE-------------------")
with open('a.txt') as f1,open('b.txt') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            pass
        else:
            print(i.strip(),j.strip())
