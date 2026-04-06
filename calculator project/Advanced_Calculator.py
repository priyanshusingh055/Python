import math

# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Cannot find square root of negative number!"
    return math.sqrt(a)

def modulus(a, b):
    return a % b


# Main Program Loop
while True:
    print("\n=== Advanced Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Exiting Calculator...")
        break

    if choice == 6:
        num = float(input("Enter number: "))
        print("Result:", square_root(num))

    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))

        elif choice == 2:
            print("Result:", subtract(num1, num2))

        elif choice == 3:
            print("Result:", multiply(num1, num2))

        elif choice == 4:
            print("Result:", divide(num1, num2))

        elif choice == 5:
            print("Result:", power(num1, num2))

        elif choice == 7:
            print("Result:", modulus(num1, num2))

        else:
            print("Invalid Choice!")