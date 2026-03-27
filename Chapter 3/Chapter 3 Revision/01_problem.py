
# Normal meathod --------------------------

# num ="Hello wolrd"

# reversed = num[::-1]

# print("Reversed String:",reversed)

# loop Meathod =============

text = "Apple"

reverse=""

for char in  text:
    reverse = char + text
    print("Revers String :",reverse)


  
  
  #. Using reversed() function *************************


text = "Python"

reverse = "".join(reversed(text))

print("Reversed string:", reverse)
