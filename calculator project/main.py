# Step 1:

# Function to add two number
def add(num1,num2):
    return num1+num2

# Function to subtract two number
def sub(num1,num2):
    return num1-num2

# Function to multiple two number
def multiply(num1,num2):
    return num1*num2

# Function to divide two number
def divide(num1,num2):
    return num1 / num2

# Function to multiple two number
def Average(num1,num2):
    return (num1 + num2)/2

# Step 2: use input

print("Please select a operation: \n" \
    "1. Addition \n" \
    "2. Subtraction \n"\
    "3. Multiply \n"\
    "4. Divide \n"\
    "5. Avgrage " )
select = int(input("Select a operation from 1,2,3,4,5:"))

number1 = int(input("Enter A Number 1:"))
number2 = int(input("Enter A Number 2:"))

# Step 3: Print the result ===========

if select ==1:
    print(f"{number1} + {number2} = {add(number1,number2)}")

elif select ==2:
    print(f"{number1} - {number2} = {sub(number1,number2)}")

elif select ==3:
    print(f"{number1} * {number2} = {multiply(number1,number2)}")  


elif select ==4:
    print(f"{number1} / {number2} = {divide(number1,number2)}")      


elif select ==5:
    print(f"( {number1} + {number2} ) /2  = {Average(number1,number2)}")

else:
    print("Error 404")
