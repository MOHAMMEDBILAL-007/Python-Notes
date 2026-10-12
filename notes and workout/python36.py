# exception handeling
try :
    inp = int(input("enter the value"))
    print(inp)
except :
    print("error has occured")

#or

try :
    inp = int(input("enter the value"))
    print(inp)
except Exception:
    print("error has occured")

#or

try :
    inp = int(input("enter the value"))
    print(inp)
except Exception as e:
    print(e)
# all above mentioned are base case except blocks
# we can specify which exception to handel and how to handel

try :
    inp = int(input("enter the value"))
    print(inp)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception:# this has to be written at the last (optional) it is like a default case
    print("error has occured")