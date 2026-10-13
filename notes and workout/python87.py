import shutil 
usage = shutil.disk_usage("c:\\")
print("total:",usage.total)
# print("used:",usage.used)
# print("free:",usage.free)
usage2 = shutil.disk_usage("D:\\")
print(usage2.total)
print(usage.total+usage2.total)
print(usage.free+usage2.free)
