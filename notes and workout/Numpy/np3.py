import numpy as np

a = np.array([[1,4,7,0,4],[1,4,2,6,8]])
b = a.copy()
print(a)
print(b)
c = np.asarray(b)
print(c)

d = np.zeros((2,3),dtype=int)# by default it is float64
print(d)
print(d.dtype)

e = np.ones((2,2))
print(e)

f = np.full((3,3),23)# all elements will be what ever i give in this case it is 23
print(f)

g = np.empty((3,3))# allocates the memory locations for the elements
print(g)

h = np.eye(4,3)# identity matrix but not a square all the time
print(h)

j = np.identity(3) # identity matrix of 3x3
print(j)

k = np.diag(j)# diagonal elements of j
print(k)

l = np.tri(3)# lower triangular matrix
print(l)

m = np.arange(1,10,1)# range 1 to 9 at 1 increment after every element
print(m)

n = np.linspace(1,10,5) # 5 elements starting from 1 to 10 with linear difference between 
print(n)

o = np.logspace(1,10,9)# 9 elements starting from 1 to 10 with logrithemic difference between each elements
print(o)

p = np.geomspace(1,10,10)# each element is multiplyed by common ratio
print(p)

q = np.random.rand(2,2)# 2x2 matrix of random elements between [0,1)]
print(q)

r = np.random.randn(2,2)# random elements 2x2 matrix including -ve numbers
print(r)

s = np.random.randint(1,9,(2,2))# 2x2 matrix of random intigers range from 1 to 8
print(s)

t = np.random.random((2,2))# 2x2 matrix of random float values
print(t)

u = np.random.choice(n,(2,3))# creats an 2x3 array with elements randomly chosen from n
print(u)

v = np.zeros_like(t)# takes the shape of t
print(v)

w = np.ones_like(t)# takes shape from t
print(w)

x = np.full_like(t,3)
print(x)
 