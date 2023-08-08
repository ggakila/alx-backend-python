import asyncio 

async def file_reply():
    await asyncio.sleep(4)
    return ("File returned")


async def data_reply():
    await asyncio.sleep(4)
    return {"data",100}

async def task1():
    print('Waiting for data')
    x = await data_reply()#while waiting fot this
    #we can have another task running
    print(x)

async def task2():
    print('Waiting for file')
    x = await file_reply()#while waiting fot this
    #we can have another task running
    print(x)

async def main():
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())

    await x
    await y

asyncio.run(task2())
