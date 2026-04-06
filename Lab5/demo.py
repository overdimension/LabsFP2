from async_map import async_map_callback, async_map, async_map_with_abort
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

#Abort
async def abort_example():
    numbers = [1, 2, 3, 4, 5]
    abort_event = asyncio.Event()

    async def trigger_abort():
        await asyncio.sleep(0.5)
        abort_event.set()

    mapping_task = asyncio.create_task(async_map_with_abort(numbers, async_square, abort_event))
    asyncio.create_task(trigger_abort())

    result = await mapping_task
    print("Abort result:", result)

#Main
def main():
    callback_example()
    asyncio.run(async_example())
    asyncio.run(abort_example())

if __name__ == "__main__":
    main()
