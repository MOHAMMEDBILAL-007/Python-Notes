import win32api
print(win32api.GetComputerName())
print(win32api.GetComputerNameEx(0))
print(win32api.GetUserName())
print(win32api.GetWindowsDirectory())
print(win32api.GetLogicalDriveStrings())
print(win32api.GetSystemDirectory())


# ________________________________________________
# from win32com import client
# speaker = client.Dispatch("SAPI.SpVoice")
# speaker.speak("hello this is your computer speaking")


