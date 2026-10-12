import numpy as np
a = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],np.float16)# by default it is int64
print(a)
print(type(a))
print(a[1,3])
print(a.shape)
print(a.dtype)
a[0,1]= 9
print(a)

b = np.insert(a,1,[[1,2,3,4,5]],axis = 0)# insert a with array at axis0 at row index 1
print(b)
print(b.size)