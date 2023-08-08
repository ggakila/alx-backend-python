import asyncio 

async def main():
    print("David went to")
    task = asyncio.create_task(foo("..to work"))
    await asyncio.sleep(0.5)
    #use taks to run when nothing is happening with foo
    # await task
    #if we want the task to still wait for foo to complete we await it
    print("finished")

async def foo(text):
    print(text)
    await asyncio.sleep(10)

asyncio.run(main())