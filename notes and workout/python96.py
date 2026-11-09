#normal multiple tasks program 
import time
# def download(filename):
#     print("waiting for server to respond")
#     time.sleep(5)
#     print(f"file {filename} downloaded ")
# download("file1")
# download("file2")
# download("file3")

#using asyncio for cuncurrent execution 
import asyncio 
async def download(filename):
    print("waiting for server to respond")
    await asyncio.sleep(5)
    print(f"file {filename} downloaded ")

async def main():
    await asyncio.gather(
        download("file1"),
        download("file2"),
        download("file3")
    )
asyncio.run(main())