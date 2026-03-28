
number = []

n = int(input("Enter How May Number :"))

for i in range(n):
    num = int(input("Enter A Number :"))
    number.append(num)


for num in number:
    if (num % 2==0):
        print("Number Is Even",num) 

    else:
        print("Number Is Odd",num)   
