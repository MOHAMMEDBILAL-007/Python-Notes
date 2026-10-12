#function arguments

# required arguments 
# a and b are the required arguments meaning we must and should give the arguments or else we will get error
def add(a,b):
    print(a+b)
# here we can give this a and b directly
add(1,2)

#default arguments 
def sub(a=1,b=2):
    print(b-a)
sub()
#here for a nd b i have given default arguments 1 and 2
sub(2,8)
#here default arguments are over_ridden by 2 and 8
sub(1)
#if i only give a single argument then it only takes for a then b uses its default values
sub(b=9)
# here it take b as 9 but takes default value of a

#key word arguments 
def div(a=6,b=2):
    print(a/2)
#here they have already given the arguments but if we need the order to be our perspective we can do like
div(b=3,a=9)
#here the compiler understands that b means b in the function also 

#variable length arguments
#here the number of argument is variable 
# the arguments are taken in the form of tuple
def avg(*values):
    sum =0
    for i in values:
        sum+=i
    print(sum/len(values))
avg(1,2,3,4)
avg(1,2)

# arguments are taken as key value pair or dictionary
def example_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
example_func(a=1, b=2)

#passing a function as an argument to another function
# functions that take another function as an argument is known sa higher order function
def sum_of_the_numbers (*a):
    return sum(a),len(a)# returns a tuple of sum and lenght
print(sum_of_the_numbers(1,2,3,4,5,6,7,8,9))

def avg_ofthe_numbers(b,c):
    return b/c

print(avg_ofthe_numbers(*sum_of_the_numbers(1,2,3,4,5,6,7)))
#using * before passing the argument because there should be 2 arguments for avg function 
# but sum functionn returns a single tuple of two elements * splits the tuple and takes each element as a single argument
# or else * is not required for sum function