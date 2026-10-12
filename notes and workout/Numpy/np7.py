import numpy as np
# 1D arrays
a = np.array([1,2,4,3])
b = np.array([6,4,9,2])
print(a+2)
print(a+b)
print(a*b)
print(a**b)
print(a/b)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.reciprocal(b))# giving int as an input makes the output also int so 0.5 becomes 0

# 2D array
c = np.array([[1,2,3,4],[2,9,3,7]],np.float64)
d = np.array([[1,5,2,4],[9,3,6,7]])

print(c+2)
print(c*d)
print(c-d)

# arthematic functions in np

print(np.min(a))
print(np.max(a))
print(np.sqrt(a))
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.reciprocal(np.cos(a)))# for secant(x)
print(f"max value in c : {np.max(a)} \nat the index : {np.argmax(a)}")

# for 2d
# to get actual cordinates use
print(np.unravel_index(np.argmax(c),c.shape))

print(np.max(c,axis=0))# axis is optional unless you want it specifically or else you can skip it to get full array operation
print(np.argmax(c,axis = 0))
print(np.sin(c))# no axis should be given
print(np.sum(c))
print(np.sum(c,axis = 0))
print(np.cumsum(a))