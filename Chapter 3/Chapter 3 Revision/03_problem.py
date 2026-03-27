#  Check if string contains a specific word



text = input("Enter sentence:")
word = input('Eneter word to search:')


if word.lower() in text.lower():
    print("word In Sentence",text)

else:
    print("Word is not Found:",word)