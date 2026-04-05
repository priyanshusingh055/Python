from functools import reduce
l = [ 100,55,44,88,33,44,5,99,101]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater,l))