class Animals:
    def __init__(self,name,gender):
        self.name = name 
        self.gender= gender 
    def sound(self):
        print("all animals make sound")
class dogs(Animals):
    def __init__(self,name,gender,breed):
        super().__init__(name,gender)
        self.name = name
        self.gender = gender 
        self.breed = breed
    def sound(self):
        super().sound()
        print("dogs bark ")
    def info(self):
        print(f"name : {self.name} \ngender : {self.gender} \nbreed : {self.breed}")

dog1 = dogs("chad","male","german shepherd")
dog1.sound()