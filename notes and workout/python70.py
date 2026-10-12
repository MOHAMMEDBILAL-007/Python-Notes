class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 

e1 = employee("killua",150000)
print(e1.name)
print(e1.salary)
# this is the normal way of usind and initalizeing the data
# but what if the data would be different 
string ="killua-150000"
e2 = employee(string.split("-")[0],string.split("-")[1])# this looks ugly and unethical
print(e2.name)
print(e2.salary)

# so we use class method for creating multiple constructors

class employee2:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 
    @classmethod
    def formstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
        # it is equivalent to calling the actual constructor

string ="killua-150000"
e3 = employee2.formstr(string)# this looke clean and ethical
print(e3.name)
print(e3.salary)
