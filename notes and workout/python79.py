class employee:
    def __init__(self,name):
        self.name = name 
    def show(self):
        print(f"name of the employee is {self.name}")
        
class gambler:
    def __init__(self,gambeling):
        self.game = gambeling
    def show(self):
        print(f"the game he won the most is {self.game}")

class gambeleremployee(gambler,employee):
    # here gambeler is first parent so when i call show first it checks in gambleremployee then gambler and then employee
    def __init__(self, name,game):
        self.name = name
        self.game = game
man = gambeleremployee("togi","poker")
print(man.name)
print(man.game)
man.show()
print(gambeleremployee.mro())