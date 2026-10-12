# import function

import math # imports the whole module and all the functions of the module are accessable
a = math.pi# here if you need to accesss a function you need a to write the math. prefix
print(a)
print(math.sqrt(9))

from math import sqrt# importing a specific function from the module
print(sqrt(9))# here to access the imported function you dont need the math. prefix

from math import *# this imports all the functions of the module 
print(pi)# you can access all the module's function without prefix math.
# this is not recommend unless you know what you need

import math as m# this is used to shorten the prefix m.
print(m.sqrt(9))# accessing the function using the shortened prefix m.

from math import sqrt as s# importing a specific function with shortened keyword
print(s(9))# square root of 9


print(dir(math))# this returns all the functions in the module

# all the above implimentations are allowed for my own module too
import my_module # importing my own module 
# this can work exactly same as the official modules
print(my_module.value)
my_module.welcom()
