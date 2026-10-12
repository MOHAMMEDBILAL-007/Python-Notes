#operations on tuple
n =(1,2,3,5,6,8,3,93,3,0)
n=list(n)
n.append(2)
n = tuple(n)
#indirect way of modifying a tuple
print(n)
n1 =(1,2,3)
n3=n+n1#concatination of tuple
n.count(3)#counts the number of times 3 is present in tuple
n.index(3)#returns the index of first 3 in tuple n
n.index(3,4,7)#returns the index of 3 which is present between the index of 4 and 7
