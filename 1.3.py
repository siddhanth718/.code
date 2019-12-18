print("Enter sides")
a,b,c=int(input().split())
p=a+b+c
s=p/2
area=s*(s-a)*(s-b)*(s-c)
print("Area",sqrt(area))