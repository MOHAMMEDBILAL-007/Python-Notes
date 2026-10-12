#loop with else
for i in range(6):# loop is fully executed then else is executed
    print(i)
else:
    print("no more i remaining")

a = []
for i in a:# loop is not entered but else is entered 
    print(i)
else:
    print("no i to print")

for i in range(6):# loop is executed till break condition here else is not executed
    print(i)
    if i ==4:
        break
else:
    print("no more i remaining")

# these methods apply to both for loop and while loop