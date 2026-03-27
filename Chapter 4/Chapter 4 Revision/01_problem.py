#  Store 5 numbers in a list and find sum  

l =[]

for i in range(5):
    num = int(input("Enter Your Value:"))
    l.append(num)

total = sum(l)


print("Number:",l)
print("Sum",total)
