#methods of functions for list
list1 =[1,4,3,6,8,4,9,5,53,4]
list1.append(99)#adds 99 at the last of the list
list1.pop()#removes the last element from the list
list1.pop(3)#removes the 3rd index element from the list
list1.clear()#removes all the elements from the list
list1.insert(1,45)#inserts 45 at index 1
list1.extend([1,2,3,4,5,3,2,1,9,8,7])#list is added to the end of the list1
#or
n =[1,2,4,2,3,5,6,4,8,6,8,5,3,9]
list1.extend(n)
#or
list1.extend(i for i in range(1,9) if i%2 ==0)#iteratable with condition
list1.remove(2)# the element at the index 2 gets deleted
list1.index(4)# gets the index of the element 4 from the list
list1.index(4[0[6]])#gets the index of the element 4 if it exist between index 0 and index 5
list1.count(2)#returns the amount of times 2 has repeated in list1
list1.sort()#sorts the elements in the asscending order
list1.sort(reverse=True)#sorts the elements in decending order
list1.reverse()#only reverse the elements of the list
list2 = list1.copy()#assaigns a copy of the list1 to the list2
