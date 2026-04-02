
class Numner :
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
      return self.n +num.n
    
n =Numner(1)
m =Numner(2)

print(n+m)