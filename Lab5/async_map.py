import asyncio

#Callback
def async_map_callback(iterable, func, callback):
    result = []
    for item in iterable:
        result.append(func(item))
    callback(result)

#Async
async def async_map(iterable, func):
    tasks = [asyncio.create_task(func(x)) for x in iterable]
    return await asyncio.gather(*tasks)

#Abort
async def async_map_with_abort(func, iterable):
    tasks = [func(x) for x in iterable]
    try:
        return await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Cancelled!")
        raise