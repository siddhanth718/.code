'''num_list=[]
n=int(input("Enter number of values for num_list: "))
print("Enter the elements:")
for i in range(n):
    num_list.append(int(input()))
'''
num_list = [1,2,3,4,1,1,2,3,1]
mode={}
for x in set(num_list):
    mode[x]=num_list.count(x)
print(mode)

m=0
for i in mode:
    if m <= mode[i]:
        m = mode[i]
print("mode =",m)
