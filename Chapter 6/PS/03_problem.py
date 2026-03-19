p1="Make A Lot Money"
p2="Buy Now"
p3="Subscribe this"
p4="Click this"


message=input("Enter Your Comment :")


if((p1 in message)or(p2 in message) or (p3 in message) or (p4 in message)):
    print("This Comment Is spam")

else:
    print("This Comment Is Not A Spam")    