# count digits in number

n = int(input("Enter Your Value :"))

count = 0

while n>0:
    n =n //10
    count = count+1
    print(count)