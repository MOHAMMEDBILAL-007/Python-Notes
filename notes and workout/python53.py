#map ,filter ,reduce

#MAP
# function for cube of a number
def cube(x):
    return x*x*x
print(cube(2))
 
# if i need to pass a list as an argument directly it will give me an error
# so we use a loop and a new list to perform the operation
l1 =[1,2,3,4,5,6,7,8]
nl1=[]
for i in l1:
    nl1.append(cube(i))
print(nl1)
# the above method is so long 

# so we use map function
nl2 =list(map(cube,l1))# map function takes 2 arguments 1 the function to perform and other on which iteratable object to perform
print(nl2)
# it can also be used to map the input to a list
lll = list(map(int,input("enter numbers seperated by commas :").split(",")))
# it can also be used to map multiple variables from a single input
x,y,z = map(int,input("enter the value of x , y , z seperated by comma :").split(','))

# FILTER
#function that checks the crediblity of the given element
def fil_fun(a):
    return a>4

#filter function filters the following list with respect to filter_function()
nl3=list(filter(fil_fun,l1))#the fil_fun must return bool datatype for every element of the l1 if true then enter the number to the list or else not entered the list
print(nl3)

#REDUCE
from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(result)