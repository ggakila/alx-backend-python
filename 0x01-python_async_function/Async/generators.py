def main(n):
    for i in range (n):
        yield i 


x = [i for i in main(10)]
print(x)

import asyncio 

async def numbers(numbers):
    for i in range(numbers):
        yield i
        await asyncio.sleep(1)

async def main():
    odd_numbers = [i async for i in numbers(10) if i % 2]
    print(odd_numbers)

asyncio.run(main())