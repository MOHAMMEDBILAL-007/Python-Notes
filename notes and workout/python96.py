#normal multiple tasks program 
# import time
# def download(filename):
#     print("waiting for server to respond")
#     time.sleep(5)
#     print(f"file {filename} downloaded ")
# download("file1")
# download("file2")
# download("file3")

#using asyncio for cuncurrent execution 
# import asyncio 
# async def download(filename):
#     print("waiting for server to respond")
#     await asyncio.sleep(5)
#     print(f"file {filename} downloaded ")

# async def main():
#     await asyncio.gather(
#         download("file1"),
#         download("file2"),
#         download("file3")
#     )
# asyncio.run(main())
# these above things are just for to understand how they work 

#1st ways to run a async function 
# import asyncio
# async def greet():
#     print("waiting")
#     await asyncio.sleep(3)
#     print("done")
# coroutine = greet()
# asyncio.run(greet())

#2nd way to run a async function
# import asyncio
# async def greet():
#     print("waiting")
#     await asyncio.sleep(3)
#     print("done")
# async def main():
#     await greet()
# asyncio.run(main())

# how to use create_task for event scheduling
# import asyncio
# async def task1():
#     print("task1 started ")
#     await asyncio.sleep(3)
#     print("task1 completed")
# async def task2():
#     print("task2 started ")
#     await asyncio.sleep(1)
#     print("task2 completed")
# async def main():
#     t1 = asyncio.create_task(task1())
#     t2= asyncio.create_task(task2())
#     await t1
#     await t2 
# asyncio.run(main())

#task cancellation 
# import asyncio 
# async def worker():
#     print("worker started")
#     try:
#         await asyncio.sleep(4)
#         print("worker completer the task")
#     except asyncio.CancelledError:
#         print("task was cancelld")
#         raise
# async def main():
#     task = asyncio.create_task(worker())
#     await asyncio.sleep(2)
#     task.cancel()
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("employer chenged his mind")
# asyncio.run(main())

# task cancellation without re-raising it
# import asyncio
# async def download():
#     print("Download started")
#     try:
#         await asyncio.sleep(4)
#         print("Download completed")
#     except asyncio.CancelledError:
#         print("Download interrupted!")
# async def main():
#     task = asyncio.create_task(download())
#     await asyncio.sleep(2)
#     task.cancel()
#     print("Cancellation requested")
#     await task
#     print("Main completed")
# asyncio.run(main())

# using asyncio.gather()
# import asyncio
# async def downloader(name,dur):
#     print(f"starting download of {name}")
#     await asyncio.sleep(dur)
#     print(f"download complete :{name}")
#     return f"succcesful : {name}"
# async def main():
#     result = await asyncio.gather(
#         downloader("image1",4),
#         downloader("image2",2),
#         downloader("image3",1)
#     )
#     return result
# print(asyncio.run(main()))

# what if one of the coroutine raises an exception 
# import asyncio
# async def task1():
#     await asyncio.sleep(1)
#     print("Task 1 completed")
#     return "Success 1"
# async def task2():
#     await asyncio.sleep(2)
#     raise ValueError("Something went wrong")
# async def task3():
#     await asyncio.sleep(3)
#     print("Task 3 completed")
#     return "Success 3"
# async def main():
#     results = await asyncio.gather(
#         task1(),
#         task2(),
#         task3(),
#         return_exceptions=True
#     )
#     print(results)
# asyncio.run(main())

#using asyncio.TaskGroup()
# import asyncio
# async def task1():
#     print("task1 started ")
#     await asyncio.sleep(3)
#     print("Task 1 completed")
#     return "Success 1"
# async def task2():
#     print("task2 started ")
#     await asyncio.sleep(2)
#     print("Task 2 completed")
#     return "Success 2"
# async def task3():
#     print("task3 started ")
#     await asyncio.sleep(1)
#     print("Task 3 completed")
#     return "Success 3"
# async def main():
#     async with asyncio.TaskGroup() as tg:
#         t1 = tg.create_task(task1())
#         t2 = tg.create_task(task2())
#         t3 = tg.create_task(task3())
#     print(t1.result(),t2.result(),t3.result())
# asyncio.run(main())

#exception group handeling
# import asyncio
# async def task1():
#     try:
#         print("Task 1 started")
#         await asyncio.sleep(5)
#         print("Task 1 completed")
#     except asyncio.CancelledError:
#         print("Task 1 cancelled!")
#         raise
# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(1)
#     raise ValueError("Something went wrong!")
# async def task3():
#     try:
#         print("Task 3 started")
#         await asyncio.sleep(5)
#         print("Task 3 completed")
#     except asyncio.CancelledError:
#         print("Task 3 cancelled!")
#         raise
# async def main():
#     try:
#         async with asyncio.TaskGroup() as tg:
#             tg.create_task(task1())
#             tg.create_task(task2())
#             tg.create_task(task3())
#     except* ValueError as e:
#         print(e)
# asyncio.run(main())

#using asyncio.wait() for all complete condition 
# import asyncio
# async def task1():
#     print("task1 started ")
#     await asyncio.sleep(3)
#     print("Task 1 completed")
#     return "Success 1"
# async def task2():
#     print("task2 started ")
#     await asyncio.sleep(2)
#     print("Task 2 completed")
#     return "Success 2"
# async def task3():
#     print("task3 started ")
#     await asyncio.sleep(1)
#     print("Task 3 completed")
#     return "Success 3"
# async def main():
#     t1= asyncio.create_task(task1())
#     t2= asyncio.create_task(task2())
#     t3= asyncio.create_task(task3())
#     done ,pending = await asyncio.wait(
#         {t1,t2,t3},
#         return_when=asyncio.ALL_COMPLETED)
#     for task in done:
#         print(task.result())
#     print("pending tasks:",len(pending))
# asyncio.run(main())

#for first complete and handeling the remaining pending tasks 
# import asyncio
# async def task1():
#     print("task1 started ")
#     await asyncio.sleep(3)
#     print("Task 1 completed")
#     return "Success 1"
# async def task2():
#     print("task2 started ")
#     await asyncio.sleep(2)
#     print("Task 2 completed")
#     return "Success 2"
# async def task3():
#     print("task3 started ")
#     await asyncio.sleep(1)
#     print("Task 3 completed")
#     return "Success 3"
# async def main():
#     t1= asyncio.create_task(task1())
#     t2= asyncio.create_task(task2())
#     t3= asyncio.create_task(task3())
#     done ,pending = await asyncio.wait(
#         {t1,t2,t3},
#         return_when=asyncio.FIRST_COMPLETED)
#     for task in done:
#         print(task.result())
#     print("pending tasks:",len(pending))
#     print("completing pending tasks")
#     # OR we can use gather here 
#     done ,pending = await asyncio.wait(
#             {t2,t3},
#             return_when=asyncio.ALL_COMPLETED)
#     for task in done:
#             print(task.result())
# asyncio.run(main())

