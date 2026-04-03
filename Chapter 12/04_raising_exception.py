
a = int(input("Enter A Number:"))
b = int(input("Enter b Number:"))
if(b == 0):
    raise ZeroDivisionError("Not Divided by zero number")
else:
   print(f"The divided by a/b = {a/b}")
