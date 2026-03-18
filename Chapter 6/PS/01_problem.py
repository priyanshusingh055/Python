number1 = int(input("Enter A Number 1:"))
number2 = int(input("Enter A Number 2:"))
number3 = int(input("Enter A Number 3:"))
number4 = int(input("Enter A Number 4 :"))

if(number1>number2 and number1>number3 and number1>number4):
    print("Greatest Number Of Number 1:",number1)

if(number2>number1 and number2>number3 and number2>number4):
    print("Greatest Number Of Number 2:",number2) 

if(number3>number2 and number3>number1 and number3>number4):
    print("Greatest Number Of Number 3:",number3)       


if(number4>number2 and number4>number3 and number4>number1):
    print("Greatest Number Of Number 4:",number4)    