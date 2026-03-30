import asyncio

#Callback
def sync_map(func, iterable):
    return [func(x) for x in iterable]

#Async
async def async_map(func, iterable):
    tasks = [func(x) for x in iterable]
    return await asyncio.gather(*tasks)

#Abort
async def async_map_with_abort(func, iterable):
    tasks = [func(x) for x in iterable]
    try:
        return await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Cancelled!")
        raise