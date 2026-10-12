import win32file
import os
print(os.getcwd())
os.chdir("D:/learning/Python-study/notes & workout")
print(os.getcwd())
win32file.CopyFile("darkblade_uids.txt","wintest.txt",False)
win32file.DeleteFile("wintest.txt")