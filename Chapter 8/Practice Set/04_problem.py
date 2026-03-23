
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

b = int(input("Enter A Number :"))
pattern(b)
