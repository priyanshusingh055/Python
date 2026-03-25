import random

def game():
    print("Yor Are Playing the game...")
    score=random.randint(1,500)
    with open("PS/hiscore.txt") as f:
        hiscore =f.read()
        if(hiscore!=""):
          hiscore =int(hiscore)
        else:
           hiscore=0 

    print(f"High Score: {hiscore}")
    print(f"You Score: {score}")
    if(score>hiscore):
       with open("PS/hiscore.txt","w") as f:
           f.write(str(score))
    return score


game()
