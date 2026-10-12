import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
co = a.copy()
print("a :",a)
print("copy :",co)
c = a.copy()
c[1]= 99# this doesent change the orignal array

vi = a.view()
print("a :",a)
print("view :",vi)
b = a.view()
b[4]=0# this changed the orignal array too 
print(a)