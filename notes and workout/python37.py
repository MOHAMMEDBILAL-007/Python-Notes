#finally key word
try :
    a = int(input("enter the number : "))
except:
    print("error has occcured")
finally:
    print("iam always executed")

# why use finally we can just print like this right
try :
    a = int(input("enter the number : "))
except:
    print("error has occcured")
print("iam always executed")
# but in a function when we return the value the below code is not executed
def fun():
    try :
        a = int(input("enter the number : "))
        return 0
    except:
        print("error has occcured")
        return 1
    print("iam always executed")# this will be left out
print(fun())

# so to avoide that we use finally key word
def fun2():
    try :
        a = int(input("enter the number : "))
        return 0
    except:
        print("error has occcured")
        return 1
    finally:
        print("iam always executed") # this is executed even after returning values

print(fun2())
