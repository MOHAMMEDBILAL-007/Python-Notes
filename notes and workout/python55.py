import random as rd
import time as t
user_point = 0
computer_point =0
def game():
    b = rd.randint(1,3)
    global user_point
    global computer_point
    user_choice = input("enter \'snake\', \'water\', \'gun\' :").lower()
    t.sleep(2)
    match b:
        case 1:
            computer_choice = "snake"
        case 2:
            computer_choice = "water"
        case 3:
            computer_choice = "gun"
        case _:
            computer_choice = "invalid choice"
    if user_choice == computer_choice:
        print(f"you choose :{user_choice}\ncomputer choose :{computer_choice}\nthis match was a draw")
    elif user_choice=="snake":
        if computer_choice == "water":
            user_point+=1
            print(f"you choose :{user_choice}\ncomputer choose :{computer_choice}\nyou won this match")
        else:
            computer_point+=1
            print(f"you choose :{user_choice}\ncomputer choose :{computer_choice}\nyou lost this match this match")
        
    elif user_choice=="water":
        if computer_choice == "gun":
            user_point+=1
            print(f"you choose :{user_choice}\ncomputer choose :{computer_choice}\nyou won this match")
        else:
            computer_point+=1
            print(f"you choose :{user_choice}\ncomputer choose :{computer_choice}\nyou lost this match this match")
        
    elif user_choice=="gun":
        if computer_choice == "snake":
            user_point+=1
            print(f"you choose :{user_choice}\ncomputer choose :{computer_choice}\nyou won this match")
        else:
            computer_point+=1
            print(f"you choose :{user_choice}\ncomputer choose :{computer_choice}\nyou lost this match this match")
    else:
        print("invalid choice")


print("you will get 3 chance try your best")
for i in range(3):
    game()
    t.sleep(2)
    print("your points :",user_point)
    t.sleep(2)
    print("computer points :",computer_point)
    t.sleep(3)