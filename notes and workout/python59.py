def intro(f):# this is a decorator that takes a function as an argument
    def mf():# modified function
        print("this function is made by darkblade")
        f()
        print("you should be thankful")   
    return mf

@intro# modify the function according to decorator
def hello():
    print("hello world")
hello()# here the modified function is called every time the orignal function is called

# the decorator can also be added like this
def bye():
    #this doesent modify the function permanently
    print("bye bro")
intro(bye)()
bye()# we can still use the orignal function

# there is a different method to implement decorators to the functions that need arguments
def intro2(f):
    def mf(*ar,**kw):
        print("this function is made by darkblade")
        f(*ar,**kw)
        print("you should be thankful")
    return mf

@intro2
def add(*a):
   print(sum(a))
add(1,2,3,4,5,6,7)

# lets take an alnalogy 
# we are building a maps for games different map is of different style
#lets create some decorators for the map
def cyberpunk(f):
    def mf(*args,**kwargs):
        print("changing the design of the buildings to cyber punk style")
        f(*args,**kwargs)
        print("successfully implemented")
    return mf
def apocalyptic(f):
    def mf(*args,**kwargs):
        print("changing the design of the buildings to ruins style")
        f(*args,**kwargs)
        print("successfully implemented")
    return mf

def building(no,avgs):
    print(f"building {no} buildings with average height of {avgs} floors ")
building(100,98)

cyberpunk(building)(200,65)

apocalyptic(building)(100,100)