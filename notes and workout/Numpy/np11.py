import numpy as np

a = np.random.randint(0,10,20)
b = np.random.randint(0,10,20)
c = np.stack((a,b),axis=0 )
print(c)
print(np.where(a == 2))
print(np.sort(a))
print(np.searchsorted(np.sort(a),[1,2,10],side='right'))

print(np.sort(c,axis =1))

# filter

arr = np.random.randint(0,11,5)
f = [True,False,True,False,True]
filtered_array = arr[f]
print(arr)
print(filtered_array)

# shuffle
d = np.array([1,2,3,4,5])
np.random.shuffle(d)
print(d)
# unique
e = np.array([19,1,2,1,2,3,3,4,5,5,4,4,6,7,7,6,8,8])
print(np.unique(e))
print(np.unique(e,return_index=True,return_counts=True))

x = np.insert(d,3,999)
print(x)

x = np.insert(d,(3,5),999)# multiple places at position 3 and 5
print(x)

d2 = np.array([[1,5,2,3],[6,2,0,5]])
d2i = np.insert(d2,2,3,axis = 0)# inserts an entair row into the matrix
print(d2i)
# same goes for append but skip the position 
