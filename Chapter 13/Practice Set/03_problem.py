
def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,55,4444,82695,725,2659,75659,365,248,33,666]

f = list(filter(divisible5,a))
print(f)