#public example
class person:
    def __init__(self):
        self.name = "dark blade"# public variable
        self.job = None# public variable
        self.age =20# public variable

p1 = person()
print(p1.name)# directly accessable outside the class
print(p1.age)# directly accessable outside the class


# private example
class man:
    def __init__(self,name):
        self.__name = name
m1 = man("n-word")
# print(m1.__name) # this raises an error
# but another indirect method to acces private is 
print(m1._man__name)


# protected example
class parent:
    def __init__(self):
        self._name = "james"
        self._job = "jobless"
class child(parent):
    pass

ch = child()
print(ch._job)
print(ch._name)