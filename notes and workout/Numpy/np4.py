import numpy as np

a = np.arange(1,100,1)
print(a)
print(a.reshape(3,33))# this doesent reshape the actual array but it returns the reshaped obj

#to reshape the actual array use
a = a.reshape(3,33)

# to flatten back to 1d use
print(a.ravel())# this doesent flatten the actual array 
print(a.flatten())#this doesent flatten the actual array 
print(a)
# do this to flatten a
a = a.ravel() 
#(or)
a = a.flatten()
print(a)
print(type(a))
print(a.shape)

a=np.resize(a,(3,33))# we can increase the no of elements in the array but the elements will be repeated
print(a)

b = np.array([[[1,2,3,4]]])
print(b.squeeze(axis=0))

print(a.sum(axis=0)) #sum of the rows
print(a.sum(axis=1))# sum of the columns

c = np.array([[1,2,3],[6,4,3],[1,5,9]])
print(c)
print(c.T)# transpose of the matrix

# iterate over the elements of the matrix

for  i in c.flat:
    print(i)

print(c.ndim)
print(c.dtype)
print(c.nbytes)
print(c.argmax())
print(c.argmin())
print(c.argsort())# rturns a list of sorted indeces
print(c.argmax(axis = 0))
print(c.argsort(axis = 0))

for i in np.nditer(c):
    print(i)
# we can provide flags like this 
nd = np.nditer(a,flags=["multi_index"])

for i in nd:
    print(nd.multi_index,i)
# one more method
for index,i in np.ndenumerate(c):
    print(index,i)