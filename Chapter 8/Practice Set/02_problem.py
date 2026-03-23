# celsius to fahrenheit
def c_to_F(f):
    return 5*(f-32)/9

f =int(input("Enter temperature is F:"))
c = c_to_F(f)
print(f"{round(c,2)}")
