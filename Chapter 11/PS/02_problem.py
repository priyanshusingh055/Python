class Employe:
    salary = 285
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = Employe()
e.salaryAfterIncrement = 385
print(e.increment)