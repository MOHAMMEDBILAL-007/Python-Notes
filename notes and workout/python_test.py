cube = lambda x : x*x*x

even_check = lambda x : x%2 ==0

a = list(map(int,input("enter a list of elements :").split(",")))

print(list(map(cube,a)))

print(list(filter(even_check,a)))

from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)#It repeatedly applies the function across the list, carrying forward the result each time.
#Think of it like folding the list from left to right
print(result)