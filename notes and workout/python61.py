# inheritance for class without constructors 
class employ:# parent class
    def info(self):
        print("name: ninja\nage: 20\nemp_ID: 203")

class programmer(employ):# child class
    def Full_info(self):
        print("programming language : python")

emp1 = programmer()
emp1.info()# this inherits parent property
emp1.Full_info()# it has its own method too


# inheritance for class with constructor
class Employ:  # Parent class
    def __init__(self, name, age, empid):
        self.name = name
        self.age = age
        self.empid = empid

    def info(self):
        return [self.name, self.age, self.empid]

class Programmer(Employ):  # Child class
    def __init__(self, name, age, empid, programming_language):
        super().__init__(name, age, empid)  # Call parent constructor
        self.pl = programming_language

    def Full_info(self):
        return self.info() + [self.pl]  # Combine parent info with programmer info

# Create a single object
p1 = Programmer("Bilal", 24, "EMP001", "Python")

print("Info:", p1.info())       # From Employ class
print("Full Info:", p1.Full_info())    # Combined info from both classes
