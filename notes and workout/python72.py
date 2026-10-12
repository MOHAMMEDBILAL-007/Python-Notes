class parent:
    def property(self):
        print("parent property inherited")

class child(parent):
    def welth(self):
        print("networth = 9999999")
    def property(self):
        print("property of the child")
    def p_property(self):
        super().property()

c1 = child()
c1.welth()
c1.property()# this calls child property even though child has inherited parent property
c1.p_property()# this will call parent property

# for __init__

class parent1:
    def __init__(self,money):
        self.money = money 

class child1(parent1):
    def __init__(self,name,age,money):
        super().__init__(money)# money is set by parent for the child
        self.name = name
        self.age = age 
c = child1("sabo",21,100000)
print(c.name)
print(c.age)
print(c.money)# money is not present in child it is set by parent


