#misalineous methods of file handling
f = open("manage 49.txt",'r')
f.seek(10)
data=f.read()#starts reading from 11th charector
print(data)
f.close()

# f = open("manage 49.txt",'w')
# f.seek(20)# if i used this the existing text will be null
# f.write("\nbro what did you do")# this is written
# f.close()

f = open("manage 49.txt",'a')
f.seek(20)# if i used this the existing text will not change
f.write("\nbro what did you do\n")# this is written at the end even seek was set to 20 it didnt start there
f.close()

#tell()
f = open("manage 49.txt",'r')
f.seek(10)
print(f.tell())# returns the position of the control
data=f.read()#starts reading from 11th charector
print(data)
f.close()

f = open("manage.txt",'w')
f.write("bro what did you do")# this is written
f.truncate(5)# even though i have written a string so long but in the file there exist only 5 charecter
f.close()