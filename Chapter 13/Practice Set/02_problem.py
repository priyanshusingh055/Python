num = int(input("Enter Number :"))
table = [str(num*i) for i in range(1,11)]


s = "\n".join(table)
print(s)