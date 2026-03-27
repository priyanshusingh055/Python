 # Find largest number in list
number =[]


for i in range(5):
    num = int(input("Enter A value:"))
    number.append(num)


largest =max(number)

print("Largest value:",largest)