# #dictionaries
# dict = {"name":"joe", "age":23,"id":2005,"country":"america"}
# print(dict) # prints the whole dictionary
# print(dict.keys())# prints only the keys of the dictionary
# print(dict.values())# prints only the values in the dictionary
# print(dict.items())# prints the key value pairs

# # accessing the elements through keys
# print(dict["name"])# if the key doesent exist then it throws an error
# print(dict["age"])
# #or
# print(dict.get("name"))#  if the key doesent exist it returns "none"
# for i in dict:# by default dictionary is iterated over keys 
#     print(i)# this only prints the keys
#     print(dict[i])# this only prints values

# for i in dict.keys():# here intentionally iterated over keys
#     print(i)
# for i in dict.values():# here intentionally iterated over values
#     print(i)

# for i,j in dict.items():# here iterated over both key and value
#     print(i,":",j)


import json 
#write
data = {"name":"uquiora","age":"unknown","life":"chill"}
with open("experiment.json",'w') as file:
    json.dump(data,file)

# read
with open("experiment.json" ,'r') as file:
    data = json.load(file)
print(data)

#append
with open("experiment.json" ,'r') as file:
    Temp_data = json.load(file)
new_data = {"name":"ragna","age":20,"life":"horrible"}
data = {1:Temp_data,2:new_data}
with open("experiment.json",'w') as file:
    json.dump(data,file,indent=4)

with open("experiment.json" ,'r') as file:
    data = json.load(file)
print(data)