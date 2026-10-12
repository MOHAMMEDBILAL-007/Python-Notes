import numpy as np
arr1 = np.array([[1,8,3],
                 [2,6,3],
                 [1,9,6]])
arr2 = np.array([[4,2,9],
                 [2,8,4],
                 [2,5,5]])
print(arr1+arr2)# corresponding elements addition
print(arr1*arr2)# corresponding elements multiplication
print(np.sqrt(arr1))
print(np.sum(arr1))
print(np.min(arr1))
print(np.max(arr1))

#finding a number in the matrix
print(np.where(arr1 >4))# returns a tuple of where the element is at axis0 ,where the element is at axis1
