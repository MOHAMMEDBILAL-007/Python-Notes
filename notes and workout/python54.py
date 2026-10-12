a = 4
b = '4'
print(a is b )# compares the identity of the objects
print(a == b)# compares the value of the objects

# 4 is created only once in the memory 
# all immutable objects are only created once
# different variables are assigned same immutable objects
a=4
b=4
print(a is b)# this will be true because int is immutable so both a and b are pointing to the same obj
print(a == b)

# but mutable objects like list is assigned to each variable seperately
a =[1,2,3,4,5,6]
b =[1,2,3,4,5,6]
print(a is b)# this will be false because both a and b are pointing seperat objects
print(a == b)

# None is an immutable object
a = None
b = None
print(a is b)
print(a is None)
print(a == b)
print(a == None)