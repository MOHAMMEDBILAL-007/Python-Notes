import os
os.chdir("d:/learning/Python-study/self learning/")# you should know by now why this is here
# file handeling in python
# reading the file
f = open("manage 49.txt",'r')
text = f.read()
print(text)
f.close()

# reads text in the form if binary
f2 = open("manage 49.txt",'rb')
text = f2.read()
print(text)
f2.close()

# writing into the file
f1 = open("manage 49.txt",'w')
f1.write("HARDEST CHOICE REQUIRS THE HARDEST WILL") # this overrides the existing text in the file
f1.close()

fi = open("new file.txt",'w')# the file doesent exist but it is created during the proccess this feature is exclusive to 'w' mode
fi.write("yo whats up bro")
fi.close()

f = open("manage 49.txt",'a')# adds the follwing lines to existing  text means appends without overriding existing text
f.write("\nits hard to see the people you made memories with slowly become ypur memory")
f.close()
# this method is too complicated because every time we open we need to make sure to close after performing the operation

# so we use 'with' keyword which automatically closes
with open("manage 49.txt",'a') as f:
    f.write("\niam not wrong what's wrong ,is this messedup world")