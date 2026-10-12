# a = [1,23,4,5]
# b = a
# b.append(23)
# b.pop(4)
# print(a)
# print(b)
list1 =[1,2,3,4,5,6]
list2 =[1,'hssh',1.23,[1,2,3]]
#indexing
print(list2[0])
print(list2[1])
print(list2[2])

#or
for i in list2:
    print(i)
#or
for i in range(0,len(list2)):
    print(list2[i])
#-ve indexing
print(list2[-1])
print(list2[-2])
#conditional statments in list
if 'hssh' in list2:
    print("True")
else:
    print("false")
#list sclicing
#list[start : end : jumpsteps]
print(list2[:])#whole list is printed by taking start as 0 by default and length of the list as the end and step is optional but taken as 1 by default
print(list2[::])# same as above
print(list2[0:])#same as above but start is given 
print(list2[0:len(list2)])# same as above
print(list2[0:-1])#in -ve indexing -1 means the last element
print(list2[::1])# step count 1
print(list2[::2])#step count 2
print(list2[0:-1:2])#all the arguments are given 

#list comprehension
#creating a list by iteratable items
list3 =[i for i in range(1,14)]#range of 1,14 is iteratable so for every i the loop iterats on the list will store the value
#we can apply condition als if we want
list4 = [i for i in range(0,9) if i%2==0 ]
print(list4)