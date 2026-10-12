class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j 
        self.k = k  
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,other):# overload the add operator to add complex numbers
        return f"{self.i + other.i}i + {self.j + other.j}j + {self.k + other.k}k"
vector1 = vector(1,2,3)
print(vector1)

vector2 = vector(4,6,3)
print(vector2)
print(vector1 + vector2)
print(type(vector1 + vector2))# the out put will be a string to make the out put as n vector also we do a little trick

class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j 
        self.k = k  
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,other):# overload the add operator to add complex numbers
        return vector(self.i + other.i,self.j + other.j,self.k + other.k)
vector1 = vector(1,2,3)
print(vector1)

vector2 = vector(4,6,3)
print(vector2)

print(vector1 + vector2)
print(type(vector1 + vector2)) # now it is vector data type

