# happy = True
# print(happy)
# print(happy:=False)
# print(happy)

# while(food :=input("enter your faveorate food :")) != "quit":
#     print(food)

l=[1,3,4,5,6,2,7,8]
# while (i:=len(l))>0:
#     print(l.pop())

result=[squares for n in l if (squares:=n*n)>20]
print(result)
