class animals:
    def __init__(self,name,species):
        self.name = name 
        self.species = species
    def display1(self):
        print(f"name of the animal : {self.name} \nspecies of the animal is: {self.species}")
class mammals:
    def __init__(self,name):
        self.name = name
    def display2(self):
        print(f"the animal is a mammal \nits name is {self.name}")
class dog(animals,mammals):
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        animals.__init__(self,name,species="dog")
        mammals.__init__(self,name)
    def display(self):
        animals.display1(self)
        mammals.display2(self)
        print(f"the breed of the dog is {self.breed}")
class goldenretriver(dog):
    def __init__(self,name,age):
        super().__init__(name,breed="golden retriver")
        self.age = age
    def display(self):
        super().display()
        print(f"age of the dog : {self.age}")

dog1 = goldenretriver("tony",13)
dog1.display()