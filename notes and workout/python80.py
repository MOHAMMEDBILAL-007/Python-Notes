class animal:
    def __init__ (self,name,species):
        self.name = name 
        self.species = species 

    def showdetails(self):
        print(f"name : {self.name}\nspecies : {self.species}")

class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name,species="dog")
        self.name = name 
        self.breed = breed
    def showdetails(self):
        super().showdetails()
        print(f'breed : {self.breed}')

class goldenretriver(dog):
    def __init__(self,name,gender):
        super().__init__(name,breed = "golden retriever")
        self.name = name 
        self.gender = gender
    def showdetails(self):
        super().showdetails()
        print(f'gender :{self.gender}')

d1 = goldenretriver("tiger","male")
d1.showdetails()