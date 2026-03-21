number = int(input("Enter Your Number :"))

for i in range(2,number):
    if(number%i) ==0:
        print("Your Number Is Not Prime")
        break
else:
    print("Your Number Is Prime")    