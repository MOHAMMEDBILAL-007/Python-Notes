# import functools
# import time
# @functools.lru_cache(maxsize=None)
# def expensive_function(n):
#     print("calculating function")
#     time.sleep(5)
#     return n*5
# print(expensive_function(5))
# print(expensive_function(2))
# print(expensive_function(4))
# #calling these again they wont wait for 5 sec every time because the results are stored in cache
# print(expensive_function(5))
# print(expensive_function(2))
# print(expensive_function(4))

from functools import lru_cache
# @lru_cache(maxsize=3)
# def square(n):
#     print(f"Calculating {n}")
#     return n * n
# print(square(2))
# print(square(4))
# print(square(6))
# #function will be executed fully for above 3
# #the cache dictionary ={2:4,4:16,6:36}
# print(square(2))
# print(square(4))
# print(square(6))
# #function will not be executed the same attributes are being used 
# print(square(8))
# # now the least recent attribute function used was 2 so to will be kicked and 8 will be added
# #the cache dictionary ={4:16,6:36,8:64} now the least recent attribute function is 4 so whatever we call next aside from those in the cache memory it will replace 4


# l=[1,2,3]
# @lru_cache
# def expensive(lis):
#     print("calculating ")
#     return sum(lis)
# print(expensive(l))

x = 10
@lru_cache
def calculate(n):
    return n + x
print(calculate(5))
x = 100
print(calculate(5))