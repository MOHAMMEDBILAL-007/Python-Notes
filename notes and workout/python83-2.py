import win32api
import win32con
import time
def alarm():
    win32api.MessageBox(0,"wake up","alarm",win32con.MB_OK)
al_time = "19 : 22 : 10"
while True:
    t = time.strftime("%H : %M : %S")
    if al_time == t:
        alarm()
        break
win32api.MessageBox(0,"hello","trial",win32con.MB_OK)
win32api.MessageBeep(0)

result = win32api.MessageBox(0,"hello","trial",0)
print(result)
win32api.MessageBox(
    0,
    "Something went wrong",
    "Error",
    win32con.MB_OK | win32con.MB_ICONEXCLAMATION | win32con.MB_TOPMOST
)
win32api.MessageBox(
    0,
    "Delete file?",
    "Warning",
    win32con.MB_YESNO | win32con.MB_ICONWARNING | win32con.MB_DEFBUTTON2
)
