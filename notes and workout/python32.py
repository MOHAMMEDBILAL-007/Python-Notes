#set methods
s1 ={1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1.union(s2))# it performs union but this doesent change the original set
print(s1)
print(s2)
s1.update(s2)# this performs union of 2 sets and store them in s1
print(s1)

print(s1.intersection(s2))# this performs intersection on s1 and s2 but doesent change the orignal set
print(s1)
print(s2)
s1.intersection_update(s2)#this performs intersection 2 sets and stores the outcome in s1
print(s1)

print(s1.symmetric_difference(s2))# performs symmitric difference 
s1.symmetric_difference_update(s2)#perform symmetric difference and stores it in the orignal set
print(s1)

s ={1,6,2,4,8,6,6,3,4,69}
print(s.difference(s2))#performs difference
s.difference_update(s2)#performs differnce and stores it in the orignal set

print(s.isdisjoint(s2)) # checks the sets are disjoint then returns bool value
print(s.issubset(s2)) # checks the set s is sub set s2 then returns bool value
print(s.issuperset(s2))# checks if s is iuper set of s2 then returns bool value


a ={1,2,3,4,5,6}
b ={9,8,7,6,5,4,3,2,1}
print(a)
a.add(7)# can add  a single element to the set 
print(a)
a.update(i for i in b)# add multiple elements to the set
print(a)
a.remove(9)# removes element from the set 
a.discard(8)# this also removes the element from set
# difference between remove() and discard() is that if the element is not prsent 
# remove() will rais an error
# discard() will not rais an error
a.pop() # this will remove a random value as set is un-ordered , and it will return the poped value
del a # this will delete the set from the code 
s2.clear() # this will not delete the set from the code but delete the all elements from set
