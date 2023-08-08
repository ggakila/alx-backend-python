import asyncio 

async def fetch_data():
    await asyncio.sleep(2)
    return {'data':100}

async def county():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(county())
    x = await(task1)
    print(x)
    await task2

asyncio.run(main())