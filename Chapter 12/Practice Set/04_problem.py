
try:
    a = int(input("Enter A:"))
    b = int(input("Enter b:"))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")    