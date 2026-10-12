class parent:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def area(self):
        return self.x * self.y

class child(parent):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (3.14 *(self.radius*self.radius))# overriding parent class
rect = parent(3,4)
print(rect.area())

circle = child(9)
print(circle.area())


#lets go complex
class parent1:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def area(self):
        return self.x * self.y
class child1(parent1):
    def __init__(self,radius,x,y):
        super().__init__(x,y)
        self.radius = radius
    def area(self):
        return (3.14 * (self.radius*self.radius))
    def morph(self):
        return (self.x*self.y)
circ= child1(4,3,4)
print(circ.area())
print(circ.morph())

