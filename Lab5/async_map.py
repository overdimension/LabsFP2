import asyncio

#Callback
def sync_map(func, iterable):
    return [func(x) for x in iterable]

#Async
async def async_map(func, iterable):
    tasks = [func(x) for x in iterable]
    return await asyncio.gather(*tasks)