n = int(input("Enter A Number : "))

with open("tables.txt", "a") as f:
    for i in range(1,11):
        f.write(f"{n} x {i} = {n*i}\n")
    f.write("\n")