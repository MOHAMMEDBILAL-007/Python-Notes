#dictionary methods
a = {"name":"joe", "age":23,"id":2005,"country":"america"}
b = {"residence" :"own house","mode of transport":"car","phone no":"1023456789"}
print(a)

a.clear()# clears the elements from the dict
print(a)

a.update(b)# updates the dict with new
print(a)

a.pop("residence")# pops the key value pair
print(a)

a.popitem()# pops the last key value pair
print(a)

del a["mode of transport"]
print(a)

print(b.__contains__("residence"))# checks for the key in the dictionarey and returns bool 
