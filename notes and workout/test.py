# print("hello","heha","kjsdbhcidsj",sep=" .. ")
# c = 1+2j
# print(type(c))
# st = """dowhat
# everyou
# wanti
# dontcare"""
# print(st)
# # for i in st:
# #     print(i)
# st ="hsdgcuuhsdhsjaihdoaisdiahsdhsdakjkjdhajska"
# print(st[3])
# print(len(st))
# print(st[:])

# import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.gmtime())
# hour = time.strftime("%H")
# minute = time.strftime("%M")
# seconds= time.strftime("%S")
# hour = int(hour)%12
# print(hour,":",int(minute),":",int(seconds))


# import time
# sttime = time.time()
# x = 0
# for i in range(1000):
#     x+=i
# print(x)
# print(time.time()-sttime)
# i = 10
# while True:
#     print(i)
#     if i >5:
#         break

# import os

# os.chdir("d:\learning\Python-study\self learning")

# with open("manage 49.txt") as f:
#     while True:
#         if not f.readline():
#             break
#         print(f.readline())
    
# def fact(x):
#     return x if x<=1 else x*fact(x-1)
# print(fact(5))
# def mfact(x):
#     f = 1
#     for i in range(1,x+1):
#         f*=i
#     return f
# print(mfact(5))

# def fib(x):
#     if x == 0 :
#         return 0
#     elif x == 1 :
#         return 1
#     else :
#         return fib(x-1)+fib(x-2)
# i = int(input("Enter till where you want to print fibonacci series : "))
# for i in range(i+1):
#     print(fib(i),end = " ")

# class coco():
#     def __init__(self,name,age):
#         self._name =name
#         self.__age = age
#     def getter(self):
#         return self._name,self.__age
# s = coco("bilal",19)
# print(*s.getter())

# class cat:
#     def __init__(self):
#         self._name = None
#         self._age = None
#     @property
#     def details(self):
#         return self._name,self._age
    
#     @details.setter
#     def details(self,det):
#         name,age = det
#         self._name = name
#         self._age = age
# s = cat()
# s.details = ("bilal",20)
# print(*s.details)
# s.name = "b"
# print(*s.details)
# print(not None)


# class Array:
#     def __init__(self,size):
#         self.size = size
#         self.array = []
#     def sizeval(self):
#         if self.size == len(self.array):
#             return True
#         else:
#             return False
#     def store(self,val):
#         self.array.append(val)
#     def display(self):
#         return self.array

# if __name__=="__main__":
#     n = int(input())
#     array1 = Array(n)
#     tl = list(map(int,input().split()))
#     for i in tl:
#         array1.store(i)
#     if array1.sizeval():
#         print(*array1.display())
# n= int(input())
# l1 = list(map(int,input().split()))[:n]
# temp1 = 0
# temp2 = -1
# it =0
# while it < len(l1)//2:
#     print(l1[temp1],l1[temp2],end=" ")
#     it +=1
#     temp1 +=1
#     temp2 -=1


# class brstr:
#     def __init__(self,string_o,string_s):
#         self.string_o = string_o
#         self.string_s = string_s
#     def bruteforce(self):
#         for i in range(len(self.string_o)-len(self.string_s)+1):
#             if self.string_o[i:i+len(self.string_s)] == self.string_s:
#                 return True
#         return False

# if __name__ == "__main__":
#     ori = input()
#     sear = input()
#     ns = brstr(ori,sear)
#     if ns.bruteforce():
#         print("string matched")
#     else :
#         print("string not matched")
# import os 
# with open("manage 49.txt",'r') as file:
#     for i in file.readlines():
#         print(i)

# class game:
#     def __new__(cls,*a,**b):
#         return super().__new__(cls)
#     def __init__(self,mode):
#         self.mode = mode
#     def movenent(self,move):
#         self.move = move
#         match move:
#             case "w":
#                 print("moving forward")
#             case "a":
#                 print("moving left")
#             case "s":
#                 print("moving backword")
#             case "d":
#                 print("moving right")
#     def stats_display(self):
#         self.strength = 33
#         self.magic = 43
#         self.stamina = 76
#         self.vision = 99
#         self.agility = 87
#         print(f"mode : {self.mode}\nstrength : {self.strength} \nmagic : {self.magic}\nstamina : {self.stamina}\nvision : {self.vision}\nagility : {self.agility}")

# class player(game):
#     def __new__(cls,*a,**b):
#         print("player created ...")
#         return super().__new__(cls)
#     def __init__(self,mode,age,gender):
#         super().__init__(mode)
#         self.mode = mode 
#         self.age = age
#         self.gender = gender
#     def player_info(self):
#         print(f"game mode {self.mode}\nage : {self.age}\ngender : male")
# m,a,g = map(str,input("enter mode of the game,age,gender seperated by \',\' :").split(',')) 
# player1 = player(m,int(a),g)
# player1.player_info()
# player1.stats_display()

# class nem:
#     def __init__(self):
#         self._vsl = 100
# nem1 = nem()
# print(nem1._vsl)

# n = int(input())
# m = int(input())

# for i in range(n,m):
#     prime=True
#     if i == 1:
#         continue
#     for j in range(2,i):
#         if i%j == 0:
#             prime = False
#             break
#     if prime:
#         print(i,end =" ")
    
# import math

# low, high = 10, 50

# for num in range(low, high + 1):

#     if num > 1 and all(num % i != 0 for i in range(2, math.isqrt(num) + 1)):

#         print(num, end=" ")
# import sympy
n=[1,2,47,3,2,234]
prev1=0
prev2=0
for i in n :
    current=max(prev1,prev2+i)
    prev2=prev1
    prev1 = current
print(prev1)