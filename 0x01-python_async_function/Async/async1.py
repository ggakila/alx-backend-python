import asyncio 

async def task1():
    print("Send email one")
    await asyncio.create_task(task2()) #makes task 1 wait for all the others 
    # task = asyncio.create_task(task2()) # it will run without waiting for the others 
    await asyncio.sleep(2)
    print("We have received the reply: email 1")

async def task2():
    print("Sent email two")
    await asyncio.create_task(task3())
    await asyncio.sleep(5)
    print("we have received reply: email 2")


async def task3():
    print("Sent email three")
    await asyncio.sleep(8)
    print("We have received reply: email 3")

asyncio.run(task1())