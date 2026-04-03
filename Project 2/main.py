import random
n = random.randint(1,100)
a= -1
geusses =0
while (a!=n):
    geusses +=1
    a = int(input("Guess The Number : "))
    if (a>n):
      print("Lower Number Please:")

    else:
     print("Higher Number Please:")

print(f"You are guess the number {n} correctly in {geusses} attempt:")   

