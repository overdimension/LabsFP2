from async_map import sync_map, async_map
import asyncio

#Callback
def square(x):
    return x * x

#Async
async def async_square(x):
    await asyncio.sleep(0.5)
    return x * x

#Test
async def main():
    numbers = [1, 2, 3, 4, 5]

    #Callback
    print("Callback result:", sync_map(square, numbers))

    #Async
    print("Async result:", await async_map(async_square, numbers))

if __name__ == "__main__":
    asyncio.run(main())
