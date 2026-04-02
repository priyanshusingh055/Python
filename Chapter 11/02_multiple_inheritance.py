
class Emplooy:
    company = "IFC"
    def show(self):
        print(f"The Name Of Emplooy{self.company} and the salary {self.language}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"out of All the language is {self.language}")



class Programme(Emplooy,coder)  :
    company ="IFC PUBLIC"
    def ShowLanguage(self):
        print(f"This Name is {self.company} his is a good with {self.language}")


a = Emplooy()
b = Programme()

b.show()
b.ShowLanguage()
b.printlanguage()


