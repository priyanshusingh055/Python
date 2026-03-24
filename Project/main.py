import random

computer = random.choice([-1,0,1])
yourstr= input("Enter  You choice:")
youDict={"s":1, "w":-1, "g":0}
your=youDict[yourstr]
reverseDict={1:"Snake",-1:"water", 0:"gun"}


print(f"You Choice {reverseDict[your]}\n Computer Choice {reverseDict [computer]}")

if(computer==your):
    print("It  a draw")

else:    
 
 if(computer==-1 and your== 1):
    print("You win!")

 elif(computer==-1 and your==0):
    print("You Lose!")  

 elif(computer==1 and your==-1 ):
    print("You Lose!")   

 elif(computer==1 and your==0):
    print("You Lose!")

 elif(computer==0 and your==-1 ):
    print("You Win!")   

 elif(computer==0 and your==1):
    print("You Lose!")   

 else:
    print("Something went wrong!")     

 