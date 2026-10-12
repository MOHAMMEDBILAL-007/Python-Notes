import numpy as np

arr1 = np.array([[1,2],[5,8]])
arr2 = np.array([[4,5],[3,0]])

mat1 = np.matrix([[1,2],[5,8]])
mat2 = np.matrix([[4,5],[3,0]])

print(type(arr1))
print(type(mat1))

print(np.add(arr1,arr2))
print(np.add(mat1,mat2))
# no difference in output

# but for multiplication
print(arr1*arr2)

# matrix multiplication
print(mat1*mat2)
print(mat1.dot(mat2))


a = np.matrix([[1,2,3,4],[8,6,4,2]])
# transpose
print(a)
print(np.transpose(a))
print(a.T)

print(np.swapaxes(a,0,1)) #swaping axis 0 with 1

# inverse
print(np.linalg.inv(mat1))# matrix must be a square matrix

# matrix power
print(np.linalg.matrix_power(mat1,3))

# determinant 
print(np.linalg.det(mat2))