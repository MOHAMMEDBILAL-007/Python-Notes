#raising custom errors
a = int(input("enter the number between 2 and 5"))
if a < 2 or a>5:
    raise ValueError("you need to enter value between 2 and 5")

# quiz

a = input("enter the number between 2 and 5")
if a == "quit":
    print("program terminated")
elif int(a) < 2 or int(a)>5:
    raise ValueError("you need to enter value between 2 and 5")
else:
    raise ValueError("enter a valid value")

