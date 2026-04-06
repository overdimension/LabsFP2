from async_map import async_map_callback, async_map
import asyncio

#Callback
def square(x):
    return x * x

def callback_example():
    numbers = [1, 2, 3, 4, 5]
    def print_result(result):
        print("Callback result:", result)
    async_map_callback(numbers, square, print_result)

#Async
async def async_square(x):
    await asyncio.sleep(0.2)
    return x * x

async def async_example():
    numbers = [1, 2, 3, 4, 5]
    result = await async_map(numbers, async_square)
    print("Async result:", result)

#Main
def main():
    callback_example()
    asyncio.run(async_example())

if __name__ == "__main__":
    main()
