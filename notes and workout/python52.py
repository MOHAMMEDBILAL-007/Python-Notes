# lambda functions

# this is a normal function
def double(x):
    return x*2
print(double(5))

#lambda function
square = lambda a :a**2
print(square(5))

# passing multiple arguments to a lambda function
avg = lambda x,y : (x+y)/2
print(avg(2,4))

# passing default arguments
CUBE_OF_3 = lambda x = 3:x*x*x
print(CUBE_OF_3())

#passing key value arguments
div = lambda x =16,y =2 : x/y
print(div(y = 6,x=24))# compiler understanda y is y in function also and x is x in function

# passing variabel length arguments
sumOF=lambda *a : sum(a)
print(sumOF(1,2,3,4,5,6,7))

# passing **kwrags 
dictionary = lambda **a: a
print(dictionary(x=1,y=3,a=2,b=4)) 
# similar to normal functions we can pass a functionas argument to another function
