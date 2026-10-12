x =[1,2,3,4,4]
print(dir(x))
print(x.__add__)

class mixt:
    """this is some thing that i have no idea of"""
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
e = mixt("luffy",20)
print(e.__dict__)
help(mixt)