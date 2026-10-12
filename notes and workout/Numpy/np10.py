import numpy as np
# join
a = np.array([1,2,3,5,4])
b = np.array([1,2,4,8,4])

print(np.concatenate((a,b)))

c = np.array([[7,3,4],[1,9,4],[9,6,2]])
d = np.array([[7,3,4],[1,9,4],[9,6,2]])
print(np.concatenate((c,d),axis=1))
print(np.concatenate((c,d),axis=0))

print(np.stack((a,b),axis = 1))
print(np.stack((c,d),axis = 0))

print(np.vstack((a,b))) # axis = 0 performs stack operation
print(np.dstack((a,b))) # axis = 1 performs stack operation

#split

e = np.array([1,2,3,4,5,6,7,8])
f = np.array([[112,233,44,55],[2,4,8,1],[11,2,34,5]])

spl = np.array_split(e,4)# split into 4 equal arrays 
print(spl)# list of array objects
print(spl[0])
print(spl[1])
print(spl[2])
print(spl[3])

nspl = np.array_split(f,3)
print(nspl)
print(nspl[0])

n1spl = np.array_split(f,4,axis=1)
print(n1spl)