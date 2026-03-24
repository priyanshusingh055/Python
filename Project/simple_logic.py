import random

computer = random.choice(["s", "w", "g"])
you = input("Enter your choice (s/w/g): ")

print("Computer chose:", computer)
print("You chose:", you)

if computer == you:
    print("Draw")
elif (you == "s" and computer == "w") or (you == "w" and computer == "g") or (you == "g" and computer == "s"):
    print("You win!")
else:
    print("You lose!")


# logic --------------

#  computer chooses Snake, Water, or Gun randomly
#    user enters choice
#  dictionary changes letters into numbers
#  program prints both choices
#  if-elif checks who wins
#   prints win, lose, or draw 