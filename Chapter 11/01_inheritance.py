
class Emplooy:
    company = "IFC"
    def show(self):
        print(f"The Name Of Emplooy{self.name} and the salary {self.salary}")





class Programme(Emplooy)  :
    company ="IFC PUBLIC"
    def ShowLanguage(self):
        print(f"This Name is {self.name} his is a good with {self.language}")


a = Emplooy()
b = Programme()

print(a.company,b.company)
