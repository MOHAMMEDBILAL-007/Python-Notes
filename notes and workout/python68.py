import os

print(f"this is the directory {os.getcwd()}")
os.chdir("C:\\Users\\mdfai\\OneDrive\\Pictures\\Screenshots")
print(f"this is the directory {os.getcwd()}")
a = os.listdir()
print(a)
for j,i in enumerate(a):
    if i.lower().endswith(".png"):
        os.rename(i,f"{j}.png")
