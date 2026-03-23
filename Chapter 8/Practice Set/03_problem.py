
def sum(n):
    if(n==1):
        return 1
    return sum (n-1)+n

b = int(input("Enter A Number:"))
print(f"Sum of Total Number: {sum(b)}")

    