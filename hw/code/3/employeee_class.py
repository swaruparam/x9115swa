class Employeee:
    
    def __init__ (self, name, age):
        self.name = name;
        self.age = age;
        
    def __repr__ (self):
        return "Employeee Name: {} \nAge: {}\n ".format(self.name, self.age)

    def __lt__ (self, other):
        return self.age < other.age


no_employees = 3


e1 = Employeee ("Charlie", 30)
e2 = Employeee ("Emily", 26)
e3 = Employeee ("Hannah", 28)
temp = Employeee

employees = [e1,e2,e3]

print "Sorting employees based on age:\n"

employees = sorted(employees)
        
for employee in employees:
    print employee.__repr__()
