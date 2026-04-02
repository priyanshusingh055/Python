

class emplooy:
    a= 1

class programmer(emplooy) :
    b = 2

class Manager(programmer):
    c = 3


o = emplooy()
print(o.a)


o = programmer()
print(o.a ,o.b)


o = Manager()
print(o.a,o.b,o.c)