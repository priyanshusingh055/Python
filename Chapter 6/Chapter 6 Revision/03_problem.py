# Find greatest of 3 numbers

a = int(input("Enter a Number:"))
b = int(input("Enter a Number:"))
c = int(input("Enter a Number:"))

# greatest = max(a,b,c)

# print("Greatest Value:",greatest)


if a>=b and a>=c:
    print("greatest Value of A:",a)

elif b>=a and b>=c:
    print("Greatest value of B:",b)
else:
    print("Greatest value is C:",c)