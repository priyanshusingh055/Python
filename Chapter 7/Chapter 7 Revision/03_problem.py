# Print factorial using loop


n = int(input("Enter Your Number :"))


facts =1

for i in range(1,n+1):
    facts *=i

print("factorial is :",facts)