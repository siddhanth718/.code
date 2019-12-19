
def solve(x):
    d={}
    for i in x:
        if x[i] not in d:
            d[x[i]] = [i]
        else:
            d[x[i]].append(i)

    print(d)

x={'apple':'fruit','cat':'mammal','mango':'fruit','dog':'mammal','beans':'veg'}

solve(x)
