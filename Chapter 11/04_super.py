

class emplooy:
    def __init__(self):
        print("Constructor of Emplooy")
    a= 1

class programmer(emplooy) :
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3


# o = emplooy()
# print(o.a)


# o = programmer()
# print(o.a ,o.b)


o = Manager()
print(o.a,o.b,o.c)