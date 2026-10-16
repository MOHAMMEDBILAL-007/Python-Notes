def mygenerator():
    for i in range(1001):
        yield i
gen = mygenerator()
print(list(gen))
# print(list(gen))
# print(next(gen))
# print(next(gen))
for i in gen:
    print(i,end =",")# this will continue after theabobe 2 next functions meaning it will start from 2

# def levelgenerator(totaldamage,kills,magicused,clevel,requirments):
#     i=clevel
#     if totaldamage >= requirments["reqdamage"] and kills>= requirments["reqkills"] and magicused>=requirments["reqmagic"]:
#         i+=1
#         for key,value in requirments.items():
#             requirments[key]*=2
#         print(f"new requirments = {requirments}")
#         yield i
#     else:
#         yield f"requirments not met"

# streq = {"reqdamage":1000,"reqkills":10,"reqmagic":100}

# while(clevel:=int(input()))<=100:
#     usdamage=int(input())
#     uskills=int(input())
#     usmagic=int(input())
#     gamelevelgenerator=levelgenerator()
# print("you have reached max level")