

number = []

n = int(input("How Many Number Enter:"))

for i in range(n):
    num =int(input("Enter A Number:"))
    number.append(num)

unique_number =set(number)

print("Unique Name :",unique_number)
    