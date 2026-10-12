import numpy as np
a = np.array([1,2,3,4])
b = np.array([[1],[2],[3],[4]])
print(np.add(a,b))

b = np.array([[1,2,3,4],[7,2,6,3],[8,3,4,5]])
print(b[0:1])
print(b[1,0:])
print(b[[0,2]])
print(b[0:3,1:3])
print(b[[0,2],:])