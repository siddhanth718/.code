import math
def is_square(x):
    if math.sqrt(x).is_integer():
        return True
    return False

def is_even(x):
    return x%2==0

n=int(input("n?"))
for i in range(1,n+1):
    if is_even(i) and is_square(i):
        print(i,end=" ")
    
