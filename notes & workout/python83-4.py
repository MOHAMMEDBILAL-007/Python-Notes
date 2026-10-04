import win32api
import win32process
import time 
import win32event
import win32con
# win32api.ShellExecute(
#     0,
#     "open",
#     "notepad.exe"
#     ,None
#     ,None
#     ,1
# )

# result = win32api.ShellExecute(0,"open","notepad.exe",None,None,1)
# print(result)
# import win32process
# import win32con
# print(win32process.STARTUPINFO())

# result = win32process.CreateProcess(
#     None,
#     "notepad.exe",
#     None,
#     None,
#     False,
#     0,
#     None,
#     None,
#     win32process.STARTUPINFO()
# )
# result = win32process.CreateProcess(
#     "C:/Windows/System32/notepad.exe",
#     "notepad.exe",
#     None,
#     None,
#     False,
#     0,
#     None,
#     None,
#     win32process.STARTUPINFO()
# )
# print(result)

# phandle,thandle,pid,tid=win32process.CreateProcess(
#     "C:/Windows/System32/notepad.exe",
#     "notepad.exe",
#     None,
#     None,
#     False,
#     0,
#     None,
#     None,
#     win32process.STARTUPINFO()
# )
# print(phandle,thandle,pid,tid)
# time.sleep(5)
# win32api.CloseHandle(phandle)
# win32api.CloseHandle(thandle)

# win32api.CloseHandle(phandle)
# win32api.CloseHandle(thandle)
# print("handle closed")

# startup = win32process.STARTUPINFO()

# phandle, thandle, pid, tid = win32process.CreateProcess(
#     r"C:\Windows\System32\notepad.exe",
#     "notepad.exe",
#     None,
#     None,
#     False,
#     0,
#     None,
#     None,
#     startup
# )

# print("PID:", pid)
# print("Process handle:", phandle)
# print("Thread handle:", thandle)

# print("Checking process...")

# exit_code = win32process.GetExitCodeProcess(phandle)

# print("Exit code:", exit_code)

# print("Starting wait...")

# result = win32event.WaitForSingleObject(
#     phandle,
#     win32event.INFINITE
# )

# print("WAIT RETURNED!")
# print("Result:", result)

# win32api.CloseHandle(thandle)
# win32api.CloseHandle(phandle)

# phandle,thandle,pid,tid = win32process.CreateProcess(
#     None,
#     r"cmd.exe",
#     None,
#     None,
#     False,
#     win32con.CREATE_NEW_CONSOLE,
#     None,
#     None,
#     win32process.STARTUPINFO()
# )
# print("PID = ",pid)
# print("waiting for cmd to close....")
# exitcode=win32process.GetExitCodeProcess(phandle)
# print(exitcode)
# Result = win32event.WaitForSingleObject(phandle,win32event.INFINITE)
# exitcode = win32process.GetExitCodeProcess(phandle)
# print(exitcode)
# print(Result)
# win32api.CloseHandle(thandle)
# win32api.CloseHandle(phandle)

# phandle,thandle,pid,tid = win32process.CreateProcess(
#     None,
#     r'cmd.exe /c "exit 25"',
#     None,
#     None,
#     False,
#     win32con.CREATE_NEW_CONSOLE,
#     None,
#     None,
#     win32process.STARTUPINFO()
# )
# print("PID = ",pid)
# print("waiting for cmd to close....")
# exitcode=win32process.GetExitCodeProcess(phandle)
# print(exitcode)
# Result = win32event.WaitForSingleObject(phandle,win32event.INFINITE)
# exitcode = win32process.GetExitCodeProcess(phandle)
# print(exitcode)
# print(Result)
# win32api.CloseHandle(thandle)
# win32api.CloseHandle(phandle)