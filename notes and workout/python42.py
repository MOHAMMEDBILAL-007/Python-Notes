marks =[13,45,67,87,65,98,56,3,44,55,1]
index = 0
for mark in marks:# here iam using a tempraory variable to calculate the iteration 
    print(mark)
    if index == 5:
        print("good")
    index +=1


# but by using enumerate function
for index,mark in enumerate(marks):# here we don't need another tempraory variable 
    print(mark)
    if index == 5:
        print("good")

for i in enumerate(marks):# here i is a tuple of index and marks 
    print(i)

for index,mark in enumerate(marks,start=2):# here index starts at 2nd iteration 
    print(mark)
    if index == 5:
        print("good")
        