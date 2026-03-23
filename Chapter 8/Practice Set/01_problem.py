
def greatest(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
    
a =int(input("Enter A Number:"))
b=int(input("Enter B Number:"))
c=int(input("Enter C Number:"))  

print(f"The Greatest value : {greatest(a,b,c)}")