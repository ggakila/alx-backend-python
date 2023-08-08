import asyncio 

async def t1():
    await t2()
    print("This is task 1")
    await t3()

async def t2():
    print("This is task 2")

async def t3():
    print("This is task 3")

asyncio.run(t1())