import random
class train :
    def __init__(self,trainNo):
        self.trainNo = trainNo
        

    def book(self ,fro, to):
        print(f"Ticket is book in train number {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"train No {self.trainNo} is running on time ")    

    def getFare(self , fro,to):
        print(f"Ticket fare  in train number {self.trainNo} from {fro} to {to} is  {random.randint(1,500)}")  

t = train(55)  
t.book("ramp" ,"Delhi")        
t.getFare("ramp" ,"Delhi")        
t.getstatus()        
     