# global variable and local variable
x = 5 # global variable
print(x)
def fun():
    y = 4#local variable
    print(y)
    print(x)# global variable is accessable through function
fun()
# print(y) # local variable cannot be accessed outside the function

x = 5#global
def fun1():
    x=4# local variable this variable is different from y above global variable
    print(x)# local variable is called

fun1()
print(x)# global x is unchanged

x =5#global variable
def fun2():
    global x # specifying that the x we use here is the same as the global variable
    x =2
    print(x)
fun2()# note : calling the function to cause the change
print(x)# orignal x changed